cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]
person = 5
for shopping_list in cook_book:
    title = shopping_list[0]
    print(title,f":\n{shopping_list[1][0][0]}, {person * shopping_list[1][0][1]}{shopping_list[1][0][2]}"
                f"\n{shopping_list[1][1][0]}, {person * shopping_list[1][1][1]}{shopping_list[1][1][2]}"
                f"\n{shopping_list[1][2][0]}, {person * shopping_list[1][2][1]}{shopping_list[1][2][2]}"
                f"\n{shopping_list[1][3][0]}, {person * shopping_list[1][3][1]}{shopping_list[1][3][2]}"
                f"\n{shopping_list[1][4][0]}, {person * shopping_list[1][4][1]}{shopping_list[1][4][2]}")
    print()
