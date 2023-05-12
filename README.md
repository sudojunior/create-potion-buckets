# create-potion-buckets

A datapack to *patch* the faulty recipe compatibility between Create and Tinkers' Construct.

## Implementation balance

- Create *thinks* a potion bucket has a ratio of **1 to 4**. (Current ratio)
- Tinkers' Construct adds the recipe as **1 to 2.5**.

If you wish to change the recipe generation, edit `amount` to whatever the spout should consume / item drain should provide for these recipes. This will only take effect for the identified potions in `potions.csv` (just vanilla potions for now).

## Incompatibility notes

Using the Cleric's from **Origins Classes** makes any potion *refined* by the class perk is rendered unusable for the recipe (as is the standard behaviour for the potion bottles).