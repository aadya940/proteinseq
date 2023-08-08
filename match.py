import os

def _readdata(
        source1: str,
        source2: str,
):
    '''
    Args
    ----
    source1: filename in current dir or string containing protein sequence
    source2: filename in current dir or string containing protein sequence

    Returns
    -------
    str
    Protein sequences
    '''
    _data1 = ""
    _data2 = ""


    # Read data and convert to string if its a file,
    # else directly if its not a file
    if source1 and source2 in os.listdir('.'):
        with open(source1, "r") as f:
            for i in f.readlines():
                _data1 += i

        with open(source2, "r") as f:
            for i in f.readlines():
                _data2 += i
    else:
        _data1 = source1
        _data2 = source2

    return str(_data1), str(_data2)

def _matchpatterns(
        seq1: str,
        seq2: str,
):
    '''
    Args
    ----
    seq1: str
        Protein Sequence 1
    seq2: str
        Protein Sequence 2

    Returns
    -------
    Dict,
        Gaps and Mismatches in Protein Sequence
    '''

    _gap1_idx = []
    _gap2_idx = []

    _mismatch = []

    # Check gaps, mismatches till the shorter sequence
    for j in range(min(len(seq1), len(seq2))):
        if seq1[j] != seq2[j]:
            _mismatch.append(j)
        if seq1[j] == "-":
            _gap1_idx.append(j)
        if seq2[j] == "-":
            _gap2_idx.append(j)

    if len(seq1) > len(seq2):
        _biggerseq = seq1
        _smallerseq = seq2
    else:
        _biggerseq = seq2
        _smallerseq = seq1


    # Check gaps for the remaining part of the longer sequence
    for j in range(len(_smallerseq), len(_biggerseq)):
        if _biggerseq[j] == "-":
            if _biggerseq == seq1:
                _gap1_idx.append(j)
            else:
                _gap2_idx.append(j)
    
    # Return the Analysis
    return {
        "Indexes of Gaps in Seq1": _gap1_idx,
        "Indexes of Gaps in Seq2": _gap2_idx,
        "Indexes of Sequence Mismatch": _mismatch,
        "Percentage of Mismatch": (len(_mismatch)/len(_smallerseq)) * 100,
        "Percentage of Match": 100 - (len(_mismatch)/len(_smallerseq)) * 100,
    }

if __name__ == "__main__":
    s1 = input("Enter name of the file containing protein sequence 1 or the sequence itself:  ")
    s2 = input("Enter name of the file containing protein sequence 2 or the sequence itself:  ")
    _seq1, _seq2 = _readdata(s1, s2)
    print(_matchpatterns(_seq1, _seq2))