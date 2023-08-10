# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update(self):
        for item in self.items:
            item.update()

class Item:

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update(self):
        if self.name == "Aged Brie": return self._AgedBrie()
        elif self.name == "Sulfuras, Hand of Ragnaros": return self._Sulfuras()
        elif self.name == "Backstage passes to a TAFKAL80ETC concert": return self._Backstage()
        elif self.name == "Conjured Mana Cake": return self._Conjured()
        else: return self._RegularItem()

    def _AgedBrie(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
    
    def _Sulfuras(self):
        pass
    
    def _Backstage(self):
        if 5 >= self.sell_in > 0:
            self.quality = self.quality + 3
        elif 10 >= self.sell_in > 5:
            self.quality = self.quality + 2
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality = self.quality + 1
        self.quality = 50 if self.quality > 50 else self.quality
        self.sell_in = self.sell_in - 1

    def _Conjured(self):
        self.quality = (self.quality - 2) if self.quality > 2 else 0
        self.sell_in = self.sell_in - 1

    def _RegularItem(self):
        if 50 > self.quality > 0:
            if self.sell_in <= 0:
                self.quality = (self.quality - 2) if self.quality > 2 else 0
            else:
                self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1

