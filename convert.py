import re

def convert_nh2t(s):
    s = s.replace('o', 'ə').replace('O','Ə').replace('u','o').replace('U','O')
    # s = s.replace('q','kw').replace('Q', 'Kw')

    # Replace non-word-initial q with kw
    s = re.sub("\Bq", "kw", s)
    s = re.sub("\BQ", "Kw", s)

    # Find indices of remaining q's
    indices = [i for i in range(len(s)) if s[i] == 'q' or s[i] == 'Q']

    return (s, indices)
        
def normalize_b(s):
    return s.replace('b', 'ə').replace('B', 'Ə')

def convert_t2nh(s):
    s = normalize_b(s).replace('o', 'u').replace('O','U').replace('ə', 'o').replace('Ə', 'O')
    # s = s.replace('kw','q').replace('Kw','Q')

    # Replace non-word-initial q with kw
    s = re.sub("\Bkw", "q", s)
    s = re.sub("\BKW", "Q", s)
    s = re.sub("\BKw", "Q", s)
    s = re.sub("\BkW", "q", s)

    # '    \n'.join(re.split())

    # Find indices of remaining kw's
    indices = [(i, i+1) for i in range(len(s) - 1) \
               if s[i].lower() == 'k' and s[i+1].lower() == 'w']
    indices = [x for sublist in indices for x in sublist]

    return (s, indices)
