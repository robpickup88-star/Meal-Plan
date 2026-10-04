# Ingredient Sources

Upload this file to your Claude Project as knowledge. It tells Claude where you
buy each ingredient.

## Settings

- **Prefer organic:** yes
- **Maximum stock cover:** 3 months. Claude can choose a bigger, cheaper pack
  (e.g. a 5 kg bag instead of 6×1 kg) as long as it's used up within this time.
- **Infinity Foods minimum order:** _(fill in, e.g. £250 ex VAT)_
- **Ocado minimum order:** _(fill in, e.g. £40)_

## Sources

| Source     | When                    | What goes there |
|------------|-------------------------|-----------------|
| `infinity` | Monthly bulk order      | Dry organic stock: grains, pulses, flours, nuts, seeds, dried fruit, tins, jars, oils, spices. Bought by the case. |
| `ocado`    | Monthly order           | Things that keep for a month: frozen food, meat and fish to freeze, long-life milk, hard cheese, cleaning items Infinity doesn't stock. |
| `fresh`    | Weekly top-up           | Perishables bought in the week they're used: fresh veg and fruit, fresh milk, bread, yoghurt, soft cheese. Buy at the shop or add to an occasional Ocado top-up order. |

## Ingredients

`Infinity code` is the product code from `infinity-foods-prices.csv`. Leave it
blank and Claude will pick the best-value product from the price list and ask
you to confirm it.

| Ingredient        | Source   | Infinity code | Product / pack            | Aisle        |
|-------------------|----------|---------------|---------------------------|--------------|
| rice              | infinity | 10513         | Brown Basmati Rice 5kg    | Pantry       |
| rolled oats       | infinity | 20530         | Rolled Oatflakes 5kg      | Pantry       |
| chia seeds        | infinity | 90528         | Chia Seeds 2kg            | Pantry       |
| kidney beans      | infinity | 390150        | Biona tins 6x400g         | Pantry       |
| chopped tomatoes  | infinity | 392130        | Mr Organic tins 12x400g   | Pantry       |
| soy sauce         | infinity | 480523        | Clearspring Tamari 6x250ml| Pantry       |
| vegetable oil     | infinity | 200529        | Clearspring Sunflower 2l  | Pantry       |
| honey             | infinity | 313105        | Essential Honey 3.18kg    | Pantry       |
| chili powder      | infinity | 9210          | Chilli Powder 6x25g       | Spices       |
| cumin             | infinity | 9216          | Ground Cumin 6x25g        | Spices       |
| chicken breast    | ocado    |               | freeze in portions        | Meat & Fish  |
| ground beef       | ocado    |               | freeze in portions        | Meat & Fish  |
| frozen berries    | ocado    |               |                           | Frozen       |
| onion             | fresh    |               |                           | Produce      |
| garlic            | fresh    |               |                           | Produce      |
| bell pepper       | fresh    |               |                           | Produce      |
| broccoli          | fresh    |               |                           | Produce      |
| milk              | fresh    |               |                           | Dairy & Eggs |
| eggs              | fresh    |               |                           | Dairy & Eggs |

Onions and garlic keep for a few weeks, so you could move them to `ocado` if
you'd rather get them in the monthly order.

## Always on hand

Staples you keep stocked. Claude lists these under "Check you still have"
instead of adding them to an order. Track how much you have in `stock.md`.

- salt
- black pepper
