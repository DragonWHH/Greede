def harisane(n):
  seke_ha = [20, 10, 5, 1]
  i = 0

  while(n>0):
    if(seke_ha[i] > n):
      i = i+1
    else:
      print(seke_ha[i])
      n = n-seke_ha[i];
  print("\n")

if __name__ == '__main__':
  for i in range(1, 21):
    harisane(i)
