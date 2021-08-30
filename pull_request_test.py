def get_even_and_odd(lst):
  final_even_lst = []
  final_odd_lst = []
  for l in lst:
    if l%2 == 0:
      final_even_lst.append(l)
    else:
      final_odd_lst.append(l)
  return final_lst
