from browser_history import get_history

outputs = get_history()

# his is a list of (datetime.datetime, url) tuples
his = outputs.histories
g=len(his)
for j in range(5):
    k=(his[j])
    print(k[1])