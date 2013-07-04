import re;


def Combinations(iterable, r):
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = range(r)
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != i + n - r:
				break
		else:
			return
		indices[i] += 1
		for j in range(i+1, r):
			indices[j] = indices[j-1] + 1
		yield tuple(pool[i] for i in indices)

def Count(username):
	pattern = r"(\w*";
	for ch in username:
		pattern = pattern + ch + r"\w*"
	pattern += ")";
	
	n = len( re.findall( pattern,text,re.IGNORECASE) );
	
	return n
	

# Get inputs
username = raw_input("First name:");
sub_len = input("Username length:");

# Initialize
minCount = -1;
minSubStr = "";
file = open("names.dic","r");
text = file.read();

#
for substr in Combinations(username,sub_len):
	jsubstr = "".join(substr);
	n = Count( jsubstr )
	
	print jsubstr + "\t" + str(n)
	
	if( minCount==-1 or n<minCount ):
		minCount = n;
		minSubStr = jsubstr;

# Print result
print minSubStr + "\t" + str(minCount)

file.close();

