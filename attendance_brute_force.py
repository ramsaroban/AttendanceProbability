#########
# Using brute_force approach
########


def generate_sequences(n, seq, results):
    if len(seq) == n:
        results.append(seq)
        return
    generate_sequences(n, seq + 'P', results)
    generate_sequences(n, seq + 'A', results)

def is_valid_sequence(seq):
    return 'AAAA' not in seq

def attendance_brute_force(N):
    all_sequences = []
    generate_sequences(N, '', all_sequences)
    
    valid_sequences = []
    for seq in all_sequences:
        if 'AAAA' not in seq:
            valid_sequences.append(seq)

    total_valid_sequences = len(valid_sequences)
    sequences_missing_graduation = []
    for seq in valid_sequences:
        if seq.endswith('A') or seq.endswith('AA') or seq.endswith('AAA'):
            sequences_missing_graduation.append(seq)

    count_missing_graduation = len(sequences_missing_graduation)
    
    return f"{count_missing_graduation}/{total_valid_sequences}"

print(attendance_brute_force(5))
print(attendance_brute_force(10))

