def min_additional_street_lamps(N, M, K, street_lamps):
   street_lamps.sort()  # Sort the positions of the street lamps
   uncovered_segments = []
   
   # Calculate the uncovered segment before the first street lamp
   uncovered_segments.append(street_lamps[0] - K)
   
   # Calculate the uncovered segments between consecutive street lamps
   for i in range(1, M):
      uncovered_segment = street_lamps[i] - street_lamps[i-1] - 2 * K
      uncovered_segments.append(uncovered_segment)
   
   # Check if the last street lamp covers the entire road
   last_segment = N - street_lamps[-1] - K
   if last_segment > 0:
      uncovered_segments.append(last_segment)
   
   # Count the number of additional street lamps needed
   additional_street_lamps = sum(segment // (2 * K + 1) + (segment % (2 * K + 1) != 0) for segment in uncovered_segments)
   
   return additional_street_lamps

# Read input
N = int(input())
M = int(input())
K = int(input())
street_lamps = [int(input()) for _ in range(M)]

# Calculate and print the minimum number of additional street lamps needed
print(min_additional_street_lamps(N, M, K, street_lamps))
