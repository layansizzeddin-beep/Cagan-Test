import csv
import sys

def main():
    try:
        data = load_data("data.csv")
    except FileNotFoundError:
        sys.exit("Could not find data.csv")
    years = []
    rates = []
    for i in range(1, len(data)):
        old = data[i - 1]["price_index"]
        new = data[i]["price_index"]
        rate = inflation_rate(old, new)
        years.append(data[i]["year"])
        rates.append(rate)
        print(data[i]["year"], round(rate, 1))
    result = summary(years, rates)
    print("Worst year:", result["peak_year"])
    print("Peak inflation (%):", round(result["peak_rate"], 1))
    print("Hyperinflation years:", result["hyper_years"])

def inflation_rate(old, new):
        if old == 0:
            raise ValueError("Old cannot be zero.")
        inflation = ((new - old)/old) * 100
        return inflation

def real_balances(money, price):
        if price == 0:
          raise ValueError("Price cannot be zero.")
        real_price = money / price
        return real_price

def is_hyperinflation(rate, yearly=False):
     if yearly:
          threshold = 12875
     else:
          threshold = 50
     return threshold < rate

def load_data(filename):
     rows = []
     with open(filename) as file:
          reader = csv.DictReader(file)
          for row in reader:
               years = int(row["year"])
               priceindex = float(row["price_index"])
               if row["money_supply"] == "":
                    money = None
               else:
                    money = float(row["money_supply"])
               rows.append({"year": years, "price_index": priceindex, "money_supply": money})
     return rows

def adaptive_expectations(rates, speed):
     if speed < 0 or speed > 1:
          raise ValueError("Speed must be between 0 and 1")
     guess = rates[0]
     guesses = [guess]
     for actual in rates[1:]:
          guess = guess + speed * (actual - guess)
          guesses.append(guess)
     return guesses

def summary(years, rates):
     peak_rate = rates[0]
     peak_year = years[0]
     hyper_years = 0
     for i in range(len(years)):
          if rates[i] > peak_rate:
               peak_rate = rates[i]
               peak_year = years[i]
          if is_hyperinflation(rates[i], yearly=True):
               hyper_years += 1
     return {"peak_year": peak_year, "peak_rate": peak_rate, "hyper_years": hyper_years}

if __name__ == "__main__":
    main()

