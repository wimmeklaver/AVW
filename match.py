from collections import defaultdict
import re


text_to_analyze = 'De man die indirecte schade veroorzaakte moet deze vergoed.'

matching_patterns = {
    'Aanprakelijkheid': ['vergoed', 'schade'],
    'Medisch': ['operatie', 'klachten']
}
result = defaultdict(int)
for category in matching_patterns:
    for pattern in matching_patterns[category]:
        if re.search(pattern, text_to_analyze):
            result[category] += 1
            
for category in result:
    print(category, '->', result[category], ' matches')

