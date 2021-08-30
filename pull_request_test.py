def get_even(lst):
  final_lst = []
  for l in lst:
    if l%2 == 0:
      final_lst.append(l)
  return final_lst
