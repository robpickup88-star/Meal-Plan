# Meal Plan Shopping Tool

Tell Claude which recipes you want to cook, and it gives you two shopping lists:

- **🛒 Bulk order**: what to add to your next bulk order, rounded up to whole
  packs.
- **🏪 Store**: what to pick up at the shop, grouped by aisle with checkboxes.

It runs inside a [Claude Project](https://claude.ai/projects), which holds your
recipe list and the rules for where you buy each ingredient.

## Files

| File | What it's for | Where it goes |
|------|---------------|---------------|
| `project-instructions.md` | Tells Claude how to build the lists | Project → **Custom instructions** |
| `recipes.md` | Your recipe book | Project → **Knowledge** |
| `ingredient-sources.md` | Bulk vs. store for each ingredient, pack sizes, staples | Project → **Knowledge** |

## Setup (about 5 minutes)

1. Go to **claude.ai → Projects → Create project**. Name it something like
   "Meal Plan".
2. Open **Set custom instructions** and paste in everything below the line in
   `project-instructions.md`.
3. Replace the example recipes in `recipes.md` with your own, then upload it to
   the Project's **Knowledge**.
   - Already have recipes somewhere else? Paste them into a chat in the Project
     and say *"Add these recipes"*. Claude will reformat them so you can copy
     them into `recipes.md`.
4. Edit `ingredient-sources.md`: mark each ingredient `bulk` or `store`, set
   the pack sizes you actually buy, and list the staples you always keep. Upload
   it to **Knowledge** too.

## Using it

Start a new chat in the Project and send something like:

```
Plan:
- Chicken Stir Fry x2
- Beef Chili (8 servings)
- Overnight Oats x5
Bulk order arrives: Thursday
Have on hand: rice 1 kg, 3 onions
```

- `x2` means make the recipe twice. `(8 servings)` scales it to 8 servings.
- **Bulk order arrives** is optional. If you give it, anything you'd need
  before the delivery goes on the store list instead.
- **Have on hand** is optional. Those items are taken off the lists.

Other things you can ask:

- *"Add this recipe: …"*: formats a recipe for `recipes.md`.
- *"Move frozen peas to bulk"*: gives you the updated line for
  `ingredient-sources.md`.
- *"Suggest two more dinners that use up the same ingredients"*: suggests
  recipes from your own book that cut down on waste.
- *"Just the store list"*: gives you only that section.

## Keeping it up to date

Project knowledge doesn't change when you edit these files, so after you change
`recipes.md` or `ingredient-sources.md`, upload the new version and delete the
old one from the Project's Knowledge. If you keep this repo on GitHub, you can
connect it to the Project instead (Knowledge → **Add content → GitHub**) and
resync after changes.

## Tips

- Use the same ingredient name in both files (`chicken breast`, not
  `chicken breasts` in one and `chicken breast fillet` in the other) so items
  combine and sort properly.
- Anything Claude can't find in `ingredient-sources.md` shows up under **Not
  sure**. Add it to the file once and it'll be sorted automatically from then
  on.
