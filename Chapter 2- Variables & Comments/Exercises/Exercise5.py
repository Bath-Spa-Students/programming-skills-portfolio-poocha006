#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left. You will to use the arithmetic operators to complete this exercise.
usb_stick_price = 10
total_budget = 35
num_usb_sticks = total_budget // usb_stick_price

remaining_pounds = total_budget % usb_stick_price

print("with $35, she can buy" , num_usb_sticks, "USB sticks.")
print("She will have $", remaining_pounds, "left.")