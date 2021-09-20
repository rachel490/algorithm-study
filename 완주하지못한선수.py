def solution(participant, completion):
    p = {}
    c = {}
    
    for x in participant:
        p[x] = p.get(x, 0) + 1
    
    for x in completion:
        c[x] = c.get(x,0) + 1

    for x in p:
        c[x] = c.get(x,0)
        if c[x] == 0 or p[x] != c[x]:
            answer = x
            
    return answer