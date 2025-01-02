

class Tree:
    def __init__(self):
        self.right = None
        self.left = None
        self.value = None

#Build the binomial tree recursively
def build_tree(node, price, up, down, period, current_period=1):

    if current_period == period:
        node.value = price
        return node.value
    
    # Create left and right children
    node.left = Tree()
    node.right = Tree()
    
    # Recursively build the children trees
    build_tree(node.left, price * down, up, down, period, current_period + 1)
    build_tree(node.right, price * up, up, down, period, current_period + 1)
    
    return node

#Calculate the option value at each step recursively
def calculate_steps(node, risk_free, up, down, exercise_price, option, prob_up, prob_down, nb_period, current_period=1):

    if current_period == nb_period:  # Leaf node
        return steps(node.value, risk_free, up, down, exercise_price, option, prob_up, prob_down, current_period)
    
    # Calculate option value recursively for child nodes
    s_left = calculate_steps(node.left, risk_free, up, down, exercise_price, option, prob_up, prob_down, nb_period, current_period + 1)
    s_right = calculate_steps(node.right, risk_free, up, down, exercise_price, option, prob_up, prob_down, nb_period, current_period + 1)
    
    node_value = ((s_right * prob_up) + (s_left * prob_down)) / (1 + risk_free)

    print(f'Nodes at period {current_period} - Up: {s_right} - Down: {s_left}')
    print(f'{option} option value of node n-1: {node_value}\n')

    return node_value


def steps(price, risk_free, up, down, exercise_price, option, prob_up, prob_down, current_period):

        right, left = price*up, price*down
        
        if option == "call":
            #Calculate the call option payoff
            C_up = max(0,right-exercise_price)
            C_down = max(0,left-exercise_price)
            
            #print("leaf up : ", C_up)
            #print("leaf down : ", C_down)
        
        elif option == "put":
            #Calculate the put option payoff
            C_up = max(0,exercise_price-right)
            C_down = max(0,exercise_price-left)
            
            #print("leaf up : ", C_up)
            #print("leaf down : ", C_down)

        #Calculate the expected option value using the risk-neutral pseudo probabilities
        value = ((C_up*prob_up)+(C_down*prob_down))
        
        #Discount back to today with the risk-free rate
        value = value/(1+risk_free)

        return value



def main():
    price = float(input("Initial asset price: ").strip()) #50
    risk_free = float(input("Risk free rate value: ").strip()) #0.07
    up = float(input("Size of up: ").strip()) #U Size of an up move (analyzed based on the volatility of the asset) #1.25
    exercise_price = float(input("Strike price: ").strip()) #45
    option = input("Option type (call/put): ").strip().lower() #call
    nb_period = int(input("Number of periods: ").strip()) #1
    down = 1/up #Size of a down move (1/U)
    
    prob_up = (1 + risk_free - down)/(up-down) #risk-neutral pseudo probability of an up-move (P(U))
    prob_down = 1-prob_up #risk-neutral pseudo probability of a down-move (P(D) = 1-P(U))
    
    root = Tree()
    build_tree(root, price, up, down, nb_period)
    
    final_value = calculate_steps(root, risk_free, up, down, exercise_price, option, prob_up, prob_down, nb_period)
    
    print(f'\nThe final {option} option value for {nb_period} periods is: {final_value}\n') #The final call option value for 1 periods is: 9.813084112149534

    return 0


if __name__ == '__main__':
    main()