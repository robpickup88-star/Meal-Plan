# Meal Plan

This repo is our household meal planner. Follow the instructions, household
details and output format in project-instructions.md:

@project-instructions.md

Those instructions were written for a Claude Project chat, which can't save
files. In Claude Code you can, so where they say "give me the updated …"
or "paste back into …", edit the file in the repo instead.

## Files

- `recipes.md`, `ingredient-sources.md`, `stock.md`, `seasonal-produce.md`:
  read these before planning. They are the source of truth.
- `infinity-foods-prices.csv`: about 5,700 products. Don't read it all;
  search it with grep (case-insensitive, by ingredient name or product
  code).
- `plans/YYYY-MM.md`: one file per month. Look at the last one before
  planning so the new month doesn't repeat it, and follow its layout.
- `price-lists/` holds the original Infinity CSVs. When a new one is added,
  run `python3 tools/slim_price_list.py price-lists/<file>.csv` to rebuild
  `infinity-foods-prices.csv`, then check every Infinity code in
  `ingredient-sources.md` still exists and flag any that don't.

## Saving changes

- **New month:** write the plan to `plans/YYYY-MM.md` (named after the month
  the plan starts in) and give a short summary in chat: the Infinity total,
  anything new to confirm, and anything under "Not sure". Mark the plan as a
  draft until we confirm it.
- **Plan confirmed** (e.g. "looks good", "order placed"): remove the draft
  label and update `stock.md` with the cupboard and freezer amounts from the
  plan. Fill in "Last updated".
- **Stock or freezer changes** we mention: update `stock.md`.
- **New recipe:** add it to `recipes.md` in the standard format and give each
  new ingredient a row in `ingredient-sources.md`, with an Infinity code for
  dry goods, chosen from the price list.
- **"Move X to …" / "Use Infinity code N for X":** update
  `ingredient-sources.md`.
- Keep ingredient names the same across `recipes.md`,
  `ingredient-sources.md` and `stock.md`.

After any change, commit with a short, plain message saying what changed (e.g.
"Add November plan", "Update stock after November order") and push.
