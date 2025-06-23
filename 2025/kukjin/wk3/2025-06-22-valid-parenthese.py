class Solution: 
    def isValid(self, s: string) -> bool: 
        stack = []
        pairs = {')':'(', '}':'{',']':'['}

        for ch in s: 
            #({[
            if ch not in pairs:
                stack.append(ch)


            # }])
            else: 
                if not stack: 
                    return False 

                if stack.pop() != pairs[ch]:
                    return False

        if not stack:
            return  True
        else:
            return False                                           

