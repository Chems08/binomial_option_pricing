# Binomial Option Pricing Model

This repository contains a Python implementation of the Binomial Option Pricing Model, which calculates the value of European options (Call and Put). 
The goal of this project was to understand the dynamics of binomial option pricing. 


## Parameters

- Initial asset price
- Risk-free interest rate
- Up and down move factors
- Risk-neutral probability of an Up and Down move
- Strike price (exercise price)
- Option type (Call or Put)
- Number of periods

## Formulas used

1. **Risk-Neutral Probabilities**:
   - ![CodeCogsEqn](https://github.com/user-attachments/assets/80037cc3-9865-465a-956e-28dfffc53f31)

   - ![CodeCogsEqn-9](https://github.com/user-attachments/assets/1e7a27b7-bab5-4d23-bf63-3fa0ea98ef85)

2. **Discounting**:
   - ![CodeCogsEqn-8](https://github.com/user-attachments/assets/3a1f7cdd-07b7-453e-b604-725195be40be)

3. **Payoff at Leaf Nodes**:
   - ![CodeCogsEqn-6](https://github.com/user-attachments/assets/de851549-2122-410d-bc94-5c181fb6b87d)

   - ![CodeCogsEqn-7](https://github.com/user-attachments/assets/32c74190-0575-47f5-94b2-8ccc31e810b8)


## Possible improvements

- Add model feature for American option
- Visualize the binomial tree structure

## Learning resources

- **PrepNuggets** (YouTube) : https://www.youtube.com/watch?v=2ac07rSaacA
- **Investopedia** : https://www.investopedia.com/terms/b/binomialoptionpricing.asp


