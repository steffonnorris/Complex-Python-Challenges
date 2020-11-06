def tile_calculator():
    length = float(input('Enter the length in feet of the room to be tiled: '))
    width = float(input('Enter the width in feet of the room to be tiled: '))
    price = float(input('Enter the price of tiles per sq.ft: '))
    disc = float(input('Enter the % discount you wish to give the customer: '))

    area = length * width
    o_amt = price * area
    disc_amt = (disc / 100) * o_amt
    final_amt = o_amt - disc_amt

    print('\n')
    print(f'Total area: {area: ,.2f} ft\N{SUPERSCRIPT TWO}')
    print(f'Price: ${o_amt: ,.2f}')
    print(f'Discount: ${disc_amt: ,.2f}')
    print(f'Discounted Price: ${final_amt: ,.2f}\n')


tile_calculator()
