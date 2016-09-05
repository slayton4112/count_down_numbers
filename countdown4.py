from operator import itemgetter

def countdown(N,T):
  # M is a map: (bitmask of used input numbers -> (expression value -> expression text))                  
  M=[{} for i in range(1<<len(N))]

  # initialize M with single-number expressions                                                           
  for i in range(len(N)):
    M[1<<i][1.0*N[i]] = "%d" % N[i]

  # allowed operators                                                                                     
  ops = (("+",lambda x,y:x+y),("-",lambda x,y:x-y),("*",lambda x,y:x*y),("/",lambda x,y:x/y))

  # enumerate all expressions                                                                             
  n=0
  while 1:

    # test to see if we're done (last iteration didn't change anything)                                   
    c=0
    for x in M: c +=len(x)
    if c==n: break
    n=c

    # loop over all values we have so far, indexed by bitmask of used input numbers                       
    for i in range(len(M)):
      for j in range(len(M)):
        if i & j: continue    # skip if both expressions used the same input number                       
        for (x,s) in M[i].items():
          for (y,t) in M[j].items():
            if y: # avoid /0 (and +0,-0,*0 while we're at it)                                             
              for (o,f) in ops:
                M[i|j][f(x,y)]="(%s%s%s)"%(s,o,t)

  # pick best expression                                                                                  
  L=[]
  for t in M:
    for(x,e) in t.items():
      if x == T:
        L+=[(abs(x-T),e)]
  L.sort();return map(itemgetter(1), L)


if __name__ == '__main__':
  #lst = [50, 75, 5, 6, 3, 2]
  lst = list(map(int, raw_input("Chosen Numbers: ").split(",")))
  print lst
  #t = 878
  t = int(raw_input("Target Number: "))
  print t
  print countdown(lst,t)