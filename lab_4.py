import heapq
import matplotlib.pyplot as plt

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(chars, freq):
    priority_queue = [Node(char, f) for char, f in zip(chars, freq)]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_node = Node(frequency=left_child.frequency + right_child.frequency)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def generate_huffman_codes(node, code="", huffman_codes={}):
    if node is not None:
        if node.symbol is not None:
            huffman_codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", huffman_codes)
        generate_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes

def visualize_huffman_tree(node, ax=None, x=0, y=0, dx=1, dy=1):
    if node is not None:
        if ax is None:
            fig, ax = plt.subplots()
        ax.text(x, y, f"{node.symbol}:{node.frequency}", ha="center", va="center", bbox=dict(facecolor='white', edgecolor='black'))
        if node.left is not None:
            ax.plot([x, x-dx], [y, y-dy], 'k-')
            visualize_huffman_tree(node.left, ax, x-dx, y-dy, dx/2, dy)
        if node.right is not None:
            ax.plot([x, x+dx], [y, y-dy], 'k-')
            visualize_huffman_tree(node.right, ax, x+dx, y-dy, dx/2, dy)

chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [4, 7, 15, 17, 22, 42]

root = build_huffman_tree(chars, freq) #build Huffman tree
huffman_codes = generate_huffman_codes(root) # Generate Huffman codes

# Print Huffman codes
for char, code in huffman_codes.items():
    print(f"Character: {char}, Code: {code}")

# Visualize Huffman tree
fig, ax = plt.subplots()
visualize_huffman_tree(root, ax)
ax.axis('off')
plt.show()
