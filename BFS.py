# Breadth First Search (EXP 4a)

graph={}
visited=[]
queue=[]
nodes=[]

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  print("The BFS traversal for the following graph is: ")

  while queue:
    s = queue.pop(0)
    nodes.remove(s)
    if not nodes:
        print (s)
    else:
        print (s, end = "-->") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

p=int(input("Enter no. of nodes in your tree, including the root node: "))
print("Please give the information on the nodes:")
for i in range(p):
    print("Enter node no.",i+1,":")
    q=input()
    nodes.append(q)

for j in range(len(nodes)):
    print("Enter child nodes of ",nodes[j],":")
    a = list(map(str,input().strip().split()))
    graph[nodes[j]]=a
print (graph)

src=input("which one is the Root Node: ")
bfs(visited,graph,src)
