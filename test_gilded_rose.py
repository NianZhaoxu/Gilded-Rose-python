# -*- coding: utf-8 -*-
import unittest
from gilded_rose import GildedRose, Item

class GildedRoseTest(unittest.TestCase):
    def test_regular_quality(self):
        items = [Item("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(39, items[0].quality)

    def test_regular_sell_in(self):
        items = [Item("bread", 20, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(19, items[0].sell_in)

    def test_regular_sell_in_passed(self):
        items = [Item("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(38, items[0].quality)

    def test_regular_sell_in_negative(self):
        items = [Item("bread", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(-1, items[0].sell_in)

    def test_regular_quality_negative(self):
        items = [Item("bread", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(0, items[0].quality)

    def test_aged_brie_quality(self):
        items = [Item("Aged Brie", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(3, items[0].quality)

    def test_aged_brie_sell_in(self):
        items = [Item("Aged Brie", 10, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(9, items[0].sell_in)

    def test_aged_brie_quality_exceeded(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(50, items[0].quality)

    def test_sulfuras_quality_unvariated(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(40, items[0].quality)

    def test_sulfuras_sell_in_unvariated(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(10, items[0].sell_in)

    def test_backstage_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(41, items[0].quality)

    def test_backstage_quality_double_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(42, items[0].quality)

    def test_backstage_quality_triple_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(43, items[0].quality)

    def test_backstage_quality_expires(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -6, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(0, items[0].quality)

    def test_backstage_quality_exceeded(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(50, items[0].quality)

    def test_backstage_sell_in(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(5, items[0].sell_in)

    def test_conjured_quality(self):
        items = [Item("Conjured Mana Cake", 6, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(0, items[0].quality)

    def test_conjured_sell_in(self):
        items = [Item("Conjured Mana Cake", 6, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(5, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
