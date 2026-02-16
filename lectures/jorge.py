def hanoi(n, source, target, intermediary):
    if (n == 1):
        print("Move disc from", source, "to", target)
    else:
        hanoi(n-1, source, intermediary, target)
        hanoi(1, source, target, intermediary)
        hanoi(n-1, intermediary, target, source)
            
