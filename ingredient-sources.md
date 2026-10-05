# Ingredient Sources

Upload this file to your Claude Project as knowledge. It tells Claude where you
buy each ingredient.

## Settings

- **Prefer organic:** yes
- **Maximum stock cover:** 3 months. Claude can choose a bigger, cheaper pack
  (e.g. a 5 kg bag instead of 6×1 kg) as long as it's used up within this time.
- **Infinity Foods minimum order:** _(fill in, e.g. £250 ex VAT)_
- **Ocado minimum order:** _(fill in, e.g. £40)_
- **Bulk fresh supplier:** _(fill in: who sells you sacks/boxes, and their
  sack sizes, e.g. onions 10 kg, carrots 10 kg, potatoes 12.5 kg)_

## Sources

| Source     | When                    | What goes there |
|------------|-------------------------|-----------------|
| `infinity` | Monthly bulk order      | Dry organic stock: grains, pulses, flours, nuts, seeds, dried fruit, tins, jars, oils, spices. Bought by the case. |
| `ocado`    | Monthly order           | Things that keep for a month: frozen food, meat and fish to freeze, long-life milk, hard cheese, cleaning items Infinity doesn't stock. |
| `bulk`     | Monthly fresh bulk      | Hardy veg and fruit that keep 3-4 weeks, bought by the sack or box at the start of the month: onions, garlic, carrots, potatoes, sweet potatoes, red cabbage, lemons, apples, satsumas. Cheaper per kg than buying weekly. |
| `fresh`    | Weekly top-up           | Perishables bought in the week they're used: fresh veg and fruit, fresh milk, bread, yoghurt, soft cheese. Buy at the shop or add to an occasional Ocado top-up order. |

## Ingredients

`Infinity code` is the product code from `infinity-foods-prices.csv`. Leave it
blank and Claude will pick the best-value product from the price list and ask
you to confirm it.

| Ingredient                | Source     | Infinity code | Product / pack                                       | Aisle        |
|---------------------------|------------|---------------|------------------------------------------------------|--------------|
| brown rice                | `infinity` | 10513         | Brown Basmati Rice 5kg                               | Pantry       |
| rolled oats               | `infinity` | 20530         | Rolled Oatflakes 5kg                                 | Pantry       |
| chia seeds                | `infinity` | 90528         | Chia Seeds 2kg                                       | Pantry       |
| green lentils             | `infinity` |               |                                                      | Pantry       |
| red lentils               | `infinity` |               |                                                      | Pantry       |
| kidney beans              | `infinity` | 390150        | Biona tins 6x400g                                    | Pantry       |
| cannellini beans          | `infinity` |               | tins                                                 | Pantry       |
| chopped tomatoes          | `infinity` | 392130        | Mr Organic tins 12x400g                              | Pantry       |
| passata                   | `infinity` |               |                                                      | Pantry       |
| tomato purée              | `infinity` |               |                                                      | Pantry       |
| sun-dried tomatoes        | `infinity` |               |                                                      | Pantry       |
| soy sauce                 | `infinity` | 480523        | Clearspring Tamari 6x250ml                           | Pantry       |
| vegetable stock           | `infinity` |               | bouillon powder (about 1 tsp per 250 ml)             | Pantry       |
| white miso                | `infinity` |               |                                                      | Pantry       |
| tahini                    | `infinity` |               |                                                      | Pantry       |
| pomegranate molasses      | `infinity` |               |                                                      | Pantry       |
| salsa                     | `infinity` |               | jar                                                  | Pantry       |
| vegan mayo                | `infinity` |               |                                                      | Pantry       |
| maple syrup               | `infinity` |               |                                                      | Pantry       |
| balsamic vinegar          | `infinity` |               |                                                      | Pantry       |
| rice vinegar              | `infinity` |               |                                                      | Pantry       |
| olive oil                 | `infinity` |               |                                                      | Pantry       |
| vegetable oil             | `infinity` | 200529        | Clearspring Sunflower 2l                             | Pantry       |
| coconut oil               | `infinity` |               |                                                      | Pantry       |
| toasted sesame oil        | `infinity` |               |                                                      | Pantry       |
| nutritional yeast         | `infinity` |               |                                                      | Pantry       |
| tempeh                    | `infinity` |               |                                                      | Pantry       |
| plant milk                | `infinity` |               | unsweetened soya drink, long-life                    | Pantry       |
| dark chocolate            | `infinity` |               |                                                      | Pantry       |
| cashews                   | `infinity` |               |                                                      | Nuts & Seeds |
| walnuts                   | `infinity` |               |                                                      | Nuts & Seeds |
| flaked almonds            | `infinity` |               |                                                      | Nuts & Seeds |
| spaghetti                 | `infinity` |               | wholewheat                                           | Pasta        |
| pasta                     | `infinity` |               | wholewheat penne or tagliatelle                      | Pasta        |
| macaroni                  | `infinity` |               | wholewheat                                           | Pasta        |
| wholewheat lasagne sheets | `infinity` |               |                                                      | Pasta        |
| chilli powder             | `infinity` | 9210          | Chilli Powder 6x25g                                  | Spices       |
| ground cumin              | `infinity` | 9216          | Ground Cumin 6x25g                                   | Spices       |
| cumin seeds               | `infinity` |               |                                                      | Spices       |
| smoked paprika            | `infinity` |               |                                                      | Spices       |
| ground coriander          | `infinity` |               |                                                      | Spices       |
| ground cinnamon           | `infinity` |               |                                                      | Spices       |
| ground allspice           | `infinity` |               |                                                      | Spices       |
| ground nutmeg             | `infinity` |               |                                                      | Spices       |
| ground cardamom           | `infinity` |               |                                                      | Spices       |
| turmeric                  | `infinity` |               |                                                      | Spices       |
| sumac                     | `infinity` |               |                                                      | Spices       |
| chilli flakes             | `infinity` |               |                                                      | Spices       |
| garlic powder             | `infinity` |               |                                                      | Spices       |
| onion powder              | `infinity` |               |                                                      | Spices       |
| dried oregano             | `infinity` |               |                                                      | Spices       |
| dried thyme               | `infinity` |               |                                                      | Spices       |
| dried basil               | `infinity` |               |                                                      | Spices       |
| bay leaves                | `infinity` |               |                                                      | Spices       |
| mustard seeds             | `infinity` |               |                                                      | Spices       |
| fenugreek seeds           | `infinity` |               |                                                      | Spices       |
| black beans               | `infinity` |               | tins                                                 | Pantry       |
| pinto beans               | `infinity` |               | tins                                                 | Pantry       |
| chickpeas                 | `infinity` |               | tins                                                 | Pantry       |
| quinoa                    | `infinity` |               |                                                      | Pantry       |
| millet                    | `infinity` |               |                                                      | Pantry       |
| gram flour                | `infinity` |               | chickpea flour                                       | Pantry       |
| date syrup                | `infinity` |               |                                                      | Pantry       |
| peanut butter             | `infinity` |               | smooth, unsalted                                     | Pantry       |
| almond butter             | `infinity` |               |                                                      | Pantry       |
| ground flaxseed           | `infinity` |               | buy whole linseed and grind a week's worth at a time | Nuts & Seeds |
| peanuts                   | `infinity` |               | unsalted                                             | Nuts & Seeds |
| sunflower seeds           | `infinity` |               |                                                      | Nuts & Seeds |
| sultanas                  | `infinity` |               |                                                      | Nuts & Seeds |
| garam masala              | `infinity` |               |                                                      | Spices       |
| curry powder              | `infinity` |               |                                                      | Spices       |
| fennel seeds              | `infinity` |               |                                                      | Spices       |
| frozen vegan gyoza        | `ocado`    |               |                                                      | Frozen       |
| bao buns                  | `ocado`    |               | frozen                                               | Frozen       |
| firm tofu                 | `ocado`    |               |                                                      | Chilled      |
| vegan butter              | `ocado`    |               |                                                      | Chilled      |
| vegan cheddar             | `ocado`    |               |                                                      | Chilled      |
| vegan parmesan            | `ocado`    |               |                                                      | Chilled      |
| corn tortillas            | `ocado`    |               |                                                      | Bakery       |
| panko breadcrumbs         | `ocado`    |               |                                                      | Pantry       |
| cornflour                 | `ocado`    |               |                                                      | Pantry       |
| bicarbonate of soda       | `ocado`    |               |                                                      | Pantry       |
| wholegrain mustard        | `ocado`    |               |                                                      | Pantry       |
| chilli garlic paste       | `ocado`    |               |                                                      | Pantry       |
| pine nuts                 | `ocado`    |               |                                                      | Nuts & Seeds |
| dried rose petals         | `ocado`    |               |                                                      | Spices       |
| asafoetida                | `ocado`    |               |                                                      | Spices       |
| white wine                | `ocado`    |               |                                                      | Drinks       |
| red wine                  | `ocado`    |               |                                                      | Drinks       |
| frozen berries            | `ocado`    |               |                                                      | Frozen       |
| frozen peas               | `ocado`    |               |                                                      | Frozen       |
| frozen spinach            | `ocado`    |               |                                                      | Frozen       |
| sweetcorn                 | `ocado`    |               | frozen                                               | Frozen       |
| wholemeal tortillas       | `ocado`    |               |                                                      | Bakery       |
| baking powder             | `ocado`    |               |                                                      | Pantry       |
| vanilla extract           | `ocado`    |               |                                                      | Pantry       |
| frozen broccoli           | `ocado`    |               |                                                      | Frozen       |
| onion                     | `bulk`     |               | sack; cool, dark, airy place                         | Produce      |
| red onion                 | `bulk`     |               | net; cool, dark, airy place                          | Produce      |
| garlic                    | `bulk`     |               | bulbs; cool and dry                                  | Produce      |
| fresh ginger              | `bulk`     |               | freeze it and grate from frozen                      | Produce      |
| carrot                    | `bulk`     |               | sack; fridge drawer or cold garage                   | Produce      |
| potatoes                  | `bulk`     |               | sack; cool and dark, not the fridge                  | Produce      |
| red cabbage               | `bulk`     |               | whole heads; fridge, 3-4 weeks                       | Produce      |
| lemon                     | `bulk`     |               | fridge, 3-4 weeks                                    | Produce      |
| sweet potato              | `bulk`     |               | box; cool room, not the fridge                       | Produce      |
| apple                     | `bulk`     |               | box; fridge, 4+ weeks                                | Produce      |
| satsuma                   | `bulk`     |               | box; fridge, 2-3 weeks                               | Produce      |
| parsnip                   | `fresh`    |               |                                                      | Produce      |
| leek                      | `fresh`    |               |                                                      | Produce      |
| fennel                    | `fresh`    |               |                                                      | Produce      |
| aubergine                 | `fresh`    |               |                                                      | Produce      |
| courgette                 | `fresh`    |               |                                                      | Produce      |
| cauliflower               | `fresh`    |               |                                                      | Produce      |
| brussels sprouts          | `fresh`    |               |                                                      | Produce      |
| mushrooms                 | `fresh`    |               |                                                      | Produce      |
| red pepper                | `fresh`    |               |                                                      | Produce      |
| tomato                    | `fresh`    |               |                                                      | Produce      |
| cucumber                  | `fresh`    |               |                                                      | Produce      |
| avocado                   | `fresh`    |               |                                                      | Produce      |
| green chilli              | `fresh`    |               |                                                      | Produce      |
| spring onion              | `fresh`    |               |                                                      | Produce      |
| lime                      | `fresh`    |               |                                                      | Produce      |
| pomegranate               | `fresh`    |               |                                                      | Produce      |
| fresh coriander           | `fresh`    |               |                                                      | Produce      |
| fresh parsley             | `fresh`    |               |                                                      | Produce      |
| fresh rosemary            | `fresh`    |               |                                                      | Produce      |
| vegan crème fraîche       | `fresh`    |               |                                                      | Chilled      |
| vegan sour cream          | `fresh`    |               |                                                      | Chilled      |
| kale                      | `fresh`    |               | or cavolo nero                                       | Produce      |
| broccoli                  | `fresh`    |               |                                                      | Produce      |
| pak choi                  | `fresh`    |               |                                                      | Produce      |
| celery                    | `fresh`    |               |                                                      | Produce      |
| cherry tomatoes           | `fresh`    |               |                                                      | Produce      |
| mango                     | `fresh`    |               |                                                      | Produce      |
| banana                    | `fresh`    |               | or other seasonal fruit                              | Produce      |
| milk                      | `fresh`    |               | dairy milk, for our daughter                         | Dairy & Eggs |
| eggs                      | `fresh`    |               | for our daughter                                     | Dairy & Eggs |

Only move something to `bulk` if it keeps for the whole month. Leafy greens,
herbs, peppers, aubergines, courgettes, tomatoes, mushrooms and avocados stay
`fresh`.

## Always on hand

Staples you keep stocked. Claude lists these under "Check you still have"
instead of adding them to an order. Track how much you have in `stock.md`.

- salt
- black pepper
- water
