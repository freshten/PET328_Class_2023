#Everyday I am getting better and better!
# input statements

# Define the function
def calculate_oil_production(nx, ny, nz, N, Pb, bob, co, ce, boi):
    # initializing output variable
    total_np = 0
    oil_per_block = []

# the 'for' loops
    for k in range(1, nz + 1):
        Pi = float(input('What is the value of initial reservoir pressure for Layer {0}?'.format(k)))
        for j in range(1, ny + 1):
            for i in range(1, nx + 1):
                block_n_order = (nx * ny * (k - 1)) + (nx * (j - 1)) + i
                Pnow = float(input('What is the current value of pressure for Block {0}?'.format(block_n_order)))
                bo = bob * (1 - (co * (Pnow - Pb)))
                block_np = (N * boi * ce * (Pi - Pnow)) / bo
                total_np += block_np
                oil_per_block.append(block_np)
                print('The cumulative oil produced from Block {0} is {1:.2f} STB'.format(block_n_order, block_np))
                
    
# returning the function result
    return total_np, oil_per_block


# input statements
# use the function int to specificy the string to an integer or whole number
# use the function float to convert the string to a number


nx = int(input('How many blocks are there in the x-axis? '))
ny = int(input('How many blocks are there in the y-axis? '))
nz = int(input('How many blocks are there in the z-axis? '))
N = float(input('What is the value of initial oil in-place STOIIP in each block? '))
Pb = float(input('What is the value of bubble point pressure? '))
bob = float(input('What is the value of oil FVF at bubble point pressure? '))
co = float(input('What is the value of oil compressibility? '))
ce = float(input('What is the value of effective compressibility? '))
boi = float(input('What is the value of initial oil FVF? '))


# calling the custom function and storing the results
total_oil_produced, oil_produced_per_block = calculate_oil_production(nx, ny, nz, N, Pb, bob, co, ce, boi)

# displaying the results
print('The total cumulative oil produced from the entire reservoir is {0:.2f} STB'.format(total_oil_produced))

# End of the code
# Ogunfuwa Teniola David

