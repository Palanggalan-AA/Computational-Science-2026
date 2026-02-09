from decimal import Decimal, getcontext, ROUND_DOWN, ROUND_HALF_UP
import math

# High precision
getcontext().prec = 120


x = 100  # you can change this value
base = Decimal("20")
scale = Decimal("3.14")

# Compute the formula
cos_val = Decimal(math.cos(x))
f = base + scale * cos_val

print(f"x = {x}")
print(f"Original value: {f}")

# Truncate and round manually for 20 decimals
truncated_20 = f.quantize(Decimal("1." + "0"*20), rounding=ROUND_DOWN)
truncated_20_str = f"{truncated_20:.20f}"
rounded_20 = truncated_20.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)
print("Decimal places 20:")
print(f"  Truncated : {truncated_20_str}")
print(f"  Rounded   : {rounded_20}")

# Truncate and round manually for 40 decimals
truncated_40 = f.quantize(Decimal("1." + "0"*40), rounding=ROUND_DOWN)
truncated_40_str = f"{truncated_40:.40f}"
rounded_40 = truncated_40.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)
print("Decimal places 40:")
print(f"  Truncated : {truncated_40_str}")
print(f"  Rounded   : {rounded_40}")

# Truncate and round manually for 60 decimals
truncated_60 = f.quantize(Decimal("1." + "0"*60), rounding=ROUND_DOWN)
truncated_60_str = f"{truncated_60:.60f}"
rounded_60 = truncated_60.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)
print("Decimal places 60:")
print(f"  Truncated : {truncated_60_str}")
print(f"  Rounded   : {rounded_60}")

# Truncate and round manually for 100 decimals
truncated_100 = f.quantize(Decimal("1." + "0"*100), rounding=ROUND_DOWN)
truncated_100_str = f"{truncated_100:.100f}"
rounded_100 = truncated_100.quantize(Decimal("1.00"), rounding=ROUND_HALF_UP)
print("Decimal places 100:")
print(f"  Truncated : {truncated_100_str}")
print(f"  Rounded   : {rounded_100}")
