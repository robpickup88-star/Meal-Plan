# Meal Plan Shopping Tool

Tell Claude what you plan to cook this month, and it works out:

- **📦 Infinity Foods order**: dry organic stock for the whole month, by the
  case, with product codes, prices and VAT.
- **🛒 Ocado monthly order**: things that keep for a month (frozen veg and
  fruit, gyoza, tofu, vegan chilled staples, etc.).
- **🥬 Weekly fresh lists**: the veg, fruit and herbs to buy from local shops
  each week, split into what's in season in the UK and what's imported (with
  seasonal swaps).
- **🧊 Freezer plan**: what goes into the freezer each week and what comes
  out, so there's always a stock of family meals and lunch tubs.
- **📋 Updated stock list**: what you'll have left over, so it isn't bought
  twice next month.

There are two ways to run it:

- **Claude Code (recommended for monthly planning):** open a Claude Code
  session on this repo at [claude.ai/code](https://claude.ai/code) or in the
  Claude app. It reads `CLAUDE.md` automatically, so it already knows the
  setup. It saves the plan, stock, recipes and sources back to GitHub for
  you.
- **Claude Project:** good for quick questions. It can read the files but
  can't save changes, so you copy anything new back into the repo yourself.

## Using Claude Code

Start a session on this repo and say what you want:

- *"Plan November"*: Claude picks recipes using your weekly rhythm and the
  season, or you can give it a list (see the format under
  [Monthly routine](#monthly-routine)). It writes `plans/2026-11.md` as a
  draft and summarises the Infinity total and anything to confirm.
- *"Looks good, order placed"*: it marks the plan final and updates
  `stock.md`.
- *"We've used up the tahini and have 2 bags of chilli in the freezer"*:
  updates `stock.md`.
- *"Add this recipe: …"*: adds it to `recipes.md`, with sources and Infinity
  codes for any new ingredients.
- *"New price list attached"*: rebuilds `infinity-foods-prices.csv` and
  checks your product codes still exist.

Every change is committed and pushed, so the next session (and the Project,
after a sync) sees it.

## Files

| File | What it's for | Where it goes |
|------|---------------|---------------|
| `CLAUDE.md` | Tells Claude Code sessions to follow `project-instructions.md` and save changes to the repo | Repo only |
| `project-instructions.md` | Tells Claude how to build the orders | Project → **Custom instructions** |
| `recipes.md` | Your recipe book | Project → **Knowledge** |
| `ingredient-sources.md` | Settings, plus Infinity / Ocado / fresh for each ingredient and the Infinity product codes you buy | Project → **Knowledge** |
| `seasonal-produce.md` | UK fruit and veg in season each month | Project → **Knowledge** |
| `stock.md` | What's already in the cupboard and freezer | Project → **Knowledge** |
| `infinity-foods-prices.csv` | Infinity Foods price list, trimmed down for Claude | Project → **Knowledge** |
| `price-lists/` | The original Infinity price lists | Keep in the repo only |
| `tools/slim_price_list.py` | Makes `infinity-foods-prices.csv` from a new price list | Run on your computer |

## Claude Project setup

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
6. Upload `recipes.md`, `ingredient-sources.md`, `stock.md`,
   `seasonal-produce.md` and `infinity-foods-prices.csv` to the Project's **Knowledge**.

You can connect this GitHub repo to the Project instead of uploading the files
(Knowledge → **Add content → GitHub**). Select those five files, then press
sync after you change them.

## Monthly routine

1. Start a Claude Code session (or a new chat in the Project) and send your plan:

   ```
   Month: November 2026
   Week 1: Lentil Bolognese, Tarka Dal x2, Smoky Lentil Tacos (10 servings), Tofu Scramble x3
   Week 2: Burnt Aubergine Veggie Chilli (8 servings), Creamy Leek Pasta x2, Lasagne
   Week 3: Aubergine & Lentil Stew (8 servings), Dumpling Soup, Bao Buns (8 servings)
   Week 4: Lentil Bolognese, Mac and Cheese, Cauliflower Shawarma, Roast Potatoes, Brussels Sprouts
   Stock changes: used up the tahini, 2 tins tomatoes left
   ```

   `x2` means cook it twice. `(8 servings)` scales the recipe to 8 servings.
   If you don't split the plan by week, Claude spreads it evenly over 4 weeks.

2. Place the **Infinity Foods** order using the codes and case numbers, and the
   **Ocado** monthly order.
3. In Claude Code, say the order's placed and `stock.md` is updated for you.
   In a Project chat, copy the **Updated stock.md** section into `stock.md`
   and re-upload or resync it.
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
