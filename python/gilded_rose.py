# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED_CAKE = "Conjured Mana Cake"

EXCEPTIONAL_ITEMS = [AGED_BRIE, BACKSTAGE_PASS, SULFURAS, CONJURED_CAKE]
LEGENDARY_ITEMS = [SULFURAS]
CONJURED_ITEMS = [CONJURED_CAKE]

def update_backstage_pass(item):

    item.quality += 1

    if item.sell_in < 11:
        item.quality += 1
    if item.sell_in < 5:
            item.quality += 1
    if item.sell_in < 0:
        item.quality = 0
    return item


def update_aged_brie(item):

    if item.quality < 50:
        item.quality += 1
    return item

def update_conjured(item):

    if item.sell_in > 0:
        item.quality -= 2
    else:
        item.quality -= 4
    return item

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            # All nonlegendary items get their sell_in decreased.
            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1

            # Deal with standard items first.
            # Quality decreases twice as fast after sell_in date has passed.
            if item.name not in EXCEPTIONAL_ITEMS:
                if item.quality > 0:
                    if item.sell_in > 0:
                        item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - 2
            else:
                if item.name == AGED_BRIE:
                    item = update_aged_brie(item)
                if item.name == BACKSTAGE_PASS:
                    item = update_backstage_pass(item)
                if item.name in CONJURED_ITEMS:
                    item = update_conjured(item)

            # Make sure no items have quality too low or high
            if item.quality > 50 and item.name != SULFURAS:
                item.quality = 50
            if item.quality < 0:
                item.quality = 0


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
