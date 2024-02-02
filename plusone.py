class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))

        # Increment the integer by one
        num += 1

        # Convert the updated integer back to a list of digits
        result = list(map(int, str(num)))

        return result
        
