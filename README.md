# Meal Plan Shopping Tool

Tell Claude what you plan to cook this month, and it works out:

- **📦 Infinity Foods order**: dry organic stock for the whole month, by the
  case, with product codes, prices and VAT.
- **🛒 Ocado monthly order**: things that keep for a month (frozen, meat to
  freeze, etc.).
- **🥬 Weekly fresh lists**: perishables for each week, to buy at the shop or
  put on an occasional Ocado top-up.
- **📋 Updated stock list**: what you'll have left over, so it isn't bought
  twice next month.

It runs inside a [Claude Project](https://claude.ai/projects), which holds your
recipes, your Infinity price list and the rules for where you buy each
ingredient.

## Files

| File | What it's for | Where it goes |
|------|---------------|---------------|
| `project-instructions.md` | Tells Claude how to build the orders | Project → **Custom instructions** |
| `recipes.md` | Your recipe book | Project → **Knowledge** |
| `ingredient-sources.md` | Settings, plus Infinity / Ocado / fresh for each ingredient and the Infinity product codes you buy | Project → **Knowledge** |
| `stock.md` | What's already in the cupboard and freezer | Project → **Knowledge** |
| `infinity-foods-prices.csv` | Infinity Foods price list, trimmed down for Claude | Project → **Knowledge** |
| `price-lists/` | The original Infinity price lists | Keep in the repo only |
| `tools/slim_price_list.py` | Makes `infinity-foods-prices.csv` from a new price list | Run on your computer |

## Setup

1. Go to **claude.ai → Projects → Create project** and name it something like
   "Meal Plan".
2. Open **Set custom instructions** and paste in everything below the line in
   `project-instructions.md`.
3. Replace the example recipes in `recipes.md` with your own.
   - Have recipes somewhere else? Paste them into a chat in the Project and say
     *"Add these recipes"*. Claude will reformat them for `recipes.md`.
4. In `ingredient-sources.md`, fill in the settings (minimum order amounts) and
   mark each ingredient `infinity`, `ocado` or `fresh`. For Infinity items, add
   the product code you buy. If you don't know it, leave it blank and Claude
   will suggest one.
5. Fill in `stock.md` with what you already have.
6. Upload `recipes.md`, `ingredient-sources.md`, `stock.md` and
   `infinity-foods-prices.csv` to the Project's **Knowledge**.

You can connect this GitHub repo to the Project instead of uploading the files
(Knowledge → **Add content → GitHub**). Select those four files, then press
sync after you change them.

## Monthly routine

1. Start a new chat in the Project and send your plan:

   ```
   Month: November 2026
   Week 1: Beef Chili x1, Chicken Stir Fry x2, Overnight Oats x5
   Week 2: Chicken Stir Fry x1, Overnight Oats x5
   Week 3: Beef Chili (8 servings), Overnight Oats x5
   Week 4: Chicken Stir Fry x2, Overnight Oats x5
   Stock changes: used up the honey, 2 tins tomatoes left
   ```

   `x2` means cook it twice. `(8 servings)` scales the recipe to 8 servings.
   If you don't split the plan by week, Claude spreads it evenly over 4 weeks.

2. Place the **Infinity Foods** order using the codes and case numbers, and the
   **Ocado** monthly order.
3. Copy the **Updated stock.md** section into `stock.md` and re-upload or
   resync it.
4. Each week, use that week's **Fresh** list at the shop, or ask *"Top-up
   order for week 2"* to get it as an Ocado basket.

Other things you can ask:

- *"Find tahini in the price list"*: lists the Infinity products, cheapest per
  kg first.
- *"Use Infinity code 5110 for red lentils"* or *"Move onions to ocado"*:
  gives you the updated row for `ingredient-sources.md`.
- *"Suggest two more dinners that use the same ingredients"*.

## When a new Infinity price list arrives

Infinity sends a new price list every two months. Save the CSV into
`price-lists/`, then run:

```
python3 tools/slim_price_list.py price-lists/<new file>.csv
```

This rewrites `infinity-foods-prices.csv` with the new prices. Re-upload it to
the Project, or resync it if the Project is linked to GitHub. Product codes in
`ingredient-sources.md` normally stay the same. If one has gone, Claude flags
it and suggests a replacement.

## Tips

- Use the same ingredient name in `recipes.md` and `ingredient-sources.md`
  (e.g. always `chopped tomatoes`) so amounts combine properly.
- Infinity prices in the list are trade case prices **excluding VAT**. Most
  food is 0% VAT. Snacks, drinks, confectionery and household items are 20%.
  Claude adds VAT line by line.
- Ingredients Claude can't place show up under **Not sure**. Add them to
  `ingredient-sources.md` once, and they'll be sorted automatically after that.
