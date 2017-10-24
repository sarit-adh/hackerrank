# https://www.hackerrank.com/challenges/ctci-making-anagrams

def number_needed(a, b):
    
    #find set of intersecting characters
    chr_list = list(set(a).intersection(set(b)))
    total_common = 0
    for chr in chr_list:
        a_total_chr = a.count(chr) 
        b_total_chr = b.count(chr)
        total_common += min(a_total_chr,b_total_chr)
         
    return (len(a) + len(b) - 2*total_common)

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
