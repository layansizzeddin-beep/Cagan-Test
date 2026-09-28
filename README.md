# Cagan Test: Syrian (Hyper)Inflation Model of Syria
#### Video Demo: https://youtu.be/y6FerssBtUE
#### Description: This project test Cagan's hyperinflation model on Syria's econony.

## What it is:
This project consists of a python programme which reads a CSV of prices and money supply and interpets it to print year inflation, the "worst" years, and how many particular years that count as hyperinflation. It features 5 functions

## Why I built it:
Coming from Syria, I experienced prices rising very fast. I am currently reading Philip Cagan's famous 1956 paper about hyperinflation, to analyse wether hyperinflation occured and when/what year and two what extent.

## The data:
I used some free online data from the World Bank. They used 2010 as the price index base and all money is measured in billions (of lira). Money data stops at 2011 as that's when the war starts.

## How it works:
The main function loads the data (using a separate function called load_data). Load_data reads the csv and turns the text into numbers. Empty money cells become "none". Inflation_rate works out percentage rise, and each year-rate is printed. Afterwards i check the inflation rate against Cagan's definition. The summary function finds the worst year and calls hyper-inflation. I also built two other functions (real_balances and adaptive expectations) and theyre ready for use but I don't have the data for it at this specific moment and context.

## Design Choices (fixes):
Missing money supply from 2012 to 2019. I cannot remove them, as 2012 - 2019 are some of Syria's most important years. Deleting them would throw away the exact period I care about, and prices still exist for those years, so inflation can still be worked out. I replaced it with "None" which clearly marks "missing", so nothing gets made up.
Cagan's rule is 50% a month. My Syria data is yearly, and 50% a month can grow into 12875% a year. The switch lets this same function handle both.
Put filename as an imput so that program isn't exclusive to Syria, and I could even potentially compare different datasets (like Germany and Zimbwawe) with it aswell!

## Tests:
5 functions are tested with pytest. There are 7 functions overall. The five cases are:
test_inflation_rate
test_real_balances
test_is_hyperinflation
test_load_data
test_adaptive_expectations

## What I found and its limits:
I found that the worst yearly inflation was about 47.7% which although was very high, (especially in my memory I remember it being ALOT!) was about 270 times smaller than 12,875% a year. Syria does NOT have hyperinflation in this sense, so either the Cagan model does not fit model war context or Syria's economy did not suffer as bad. However, yearly averages hide particularly bad months. Also, money data is missing for the war years.
