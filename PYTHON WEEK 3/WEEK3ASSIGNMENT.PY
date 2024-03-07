def calculate_discount(price, discount_percent):
    # Convert inputs to float
    price = float(price)
    discount_percent = float(discount_percent)
    
    # Check if the discount is applicable
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    original_price = input("Enter the original price of the item: ")
    discount_percentage = input("Enter the discount percentage: ")
    
    # Calculate the final price after the discount
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Convert original_price to float for comparison since final_price is a float
    original_price = float(original_price)
    
    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount was applied. The original price is: ${original_price:.2f}")

if __name__ == "__main__":
    main()
