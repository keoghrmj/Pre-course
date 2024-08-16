from collections import Counter


def topKFrequent(words, k):
    freq_count = {}
    most_comm = []
    for word in words:
        if word in freq_count:
            freq_count[word] += 1
        else:
            freq_count[word] = 1
    x = Counter(freq_count)
    most_comm = x.most_common(k)
    most_comm_keys = []
    for i in most_comm:
        most_comm_keys.append(i[0])
    most_comm_keys.sort()
    return most_comm_keys


print(topKFrequent(["the", "day", "is", "sunny",
      "the", "the", "the", "sunny", "is", "is"], 4))
