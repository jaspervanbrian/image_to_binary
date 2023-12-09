import matplotlib.pyplot as plt

print("\n")
print("This is the Binary to Image (Pyplot) program.")
print("You will be asked to input a 2D binary array with n x n dimensions.")
print("Input only accepts 1 and 0s for it to work properly, and  must be strictly separated with space.")
print("\n")
print("Example input:")
print("0 0 1 0 0")
print("0 0 1 0 0")
print("1 1 1 1 1")
print("0 0 1 0 0")
print("0 0 1 0 0")
print("\n")
print("This will generate a white cross. Note that 1 will be deemed as white and 0 will result in black color.")
print("\n")

# Ask the user to input size in n
size = int(input("Enter the number of size n of the binary: "))
print('\nInput your 2D binary array separated by space:')

# Initializing the matrix  
example_matrix = []

# Taking Rows x Columns matrix from the user  
for i in range(size):
    # taking input for the row from the user  
    single_row = list(map(int, input().split()))
    # appending the 'single_row' to the 'example_matrix'  
    example_matrix.append(single_row)

# Display the binary image
plt.title('Binary Image')
plt.imshow(example_matrix, cmap='gray')
plt.show()
