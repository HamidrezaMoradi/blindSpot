import math
from glob import glob
import sys

from PIL import Image


class BlindSpot(object):
    """
    The blindSpot can make a mosaic image for you using the photos you give.

    You can send the following parameters
    mainImage and tilesPath
    and to make use of the method of mosaicByNumTiles ()
    More methods will be added soon.
    """
    def __init__(self, mainImage, tilesPath):
        self.__originalImage = Image.open(mainImage)
        self.__originalImage = self.__originalImage.resize((self.__originalImage.width * 2, self.__originalImage.height * 2)).convert('RGB')

        self.__tiles = list()
        if tilesPath[-1] == "/":
            self.tilesPath = tilesPath + '*'
        else:
            self.tilesPath = tilesPath + '/*'

        for tile in glob(self.tilesPath):
            try:
                self.__tiles.append(Image.open(tile))
            except IOError:
                pass
        if len(self.__tiles) is 0:
            return 'error' # TODO: change this

    def mosaicByNumTiles(self, numberOfVerticalTiles = 150, numberOfHorizontalTiles = 150, enlargement = 10):
        self.numberOfVerticalTiles = numberOfVerticalTiles
        self.numberOfHorizontalTiles = numberOfHorizontalTiles

        self.enlargement = enlargement

        self.__tilesData = self.__tilesProcessor()

        width = self.__originalImage.width / (numberOfVerticalTiles * 1.0)
        height = self.__originalImage.height / (numberOfHorizontalTiles * 1.0)
        (left, upper, right, lower) = (0, 0, width, height)

        bestFitImages = list()
        min_diff = sys.maxsize
        for x in range(0, numberOfHorizontalTiles):
            (left, right) = (0, width)
            for y in range(0, int(numberOfVerticalTiles)):
                crop = self.__originalImage.crop((left, upper, right, lower))
                left = left + width
                right = right + width
                index = 0
                minDiff = sys.maxsize
                for tileData in self.__tilesData:
                    diff = self.__compare(crop.getdata(), tileData)
                    if diff < minDiff:
                        minDiff = diff
                        bestFit = self.__tiles[index]
                    index += 1
                bestFitImages.append(bestFit)
            crop = self.__originalImage.crop((left, upper, right, lower))
            upper = upper + height
            lower = lower + height

        return self.__buildMosaic(bestFitImages, crop)

    def __tilesProcessor(self):
        tilesData = list(map(lambda tile: list(tile.resize((int(self.__originalImage.width / self.numberOfVerticalTiles + 1),
                                                             int(self.__originalImage.height / self.numberOfHorizontalTiles + 1))).convert(
                                                             'RGB').getdata()), self.__tiles))

        return tilesData

    def __compare(self, crop, tileData):
        # Find the most appropriate image
        diff = 0
        for i in range(len(crop)):
            diff += (abs(crop[i][0] - tileData[i][0]) + abs(crop[i][1] - tileData[i][1]) + abs(
                crop[i][2] - tileData[i][2]))
            if diff > sys.maxsize:
                return diff
        return diff

    def __buildMosaic(self, tiles, crop):
        # Creating mosaic image
        width = crop.size[0] * self.enlargement
        height = crop.size[1] * self.enlargement
        mosaicWidth = width * self.numberOfVerticalTiles
        mosaicHeight = height * self.numberOfHorizontalTiles
        mosaic = Image.new("RGB", (int(mosaicWidth), int(mosaicHeight)), "White")
        column = 0
        row = 0
        for tile in tiles:
            if column != 0 and column % self.numberOfVerticalTiles == 0:
                row += 1
                column = 0
            pos = (width * column, height * row)
            tile = tile.resize((width, height))
            mosaic.paste(tile, pos)
            column += 1
        return mosaic


    @property
    def getTiles(self):
        return self.__tiles

    @property
    def getOriginalImage(self):
        return self.__originalImage