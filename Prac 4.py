from fuzzywuzzy import fuzz
from fuzzywuzzy import process
S1 = "9867593438"
S2 = "8169416295"

print("Fuzzywuzzy Ratio:",fuzz.ratio(S1,S2))
print("Fuzzywuzzy PartialRatio:",fuzz.partial_ratio(S1,S2))
print("Fuzzywuzzy TokenSortRatio:",fuzz.token_sort_ratio(S1,S2))
print("Fuzzywuzzy TokenSetRatio:",fuzz.token_set_ratio(S1,S2))
print("Fuzzywuzzy WRatio:",fuzz.WRatio(S1,S2),'\n\n')