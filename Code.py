class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(expr):
            if expr.isdigit():
                return [int(expr)]
            results = []
            for i, char in enumerate(expr):
                if char in '+-*':
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    for l in left:
                        for r in right:
                            if char == '+':
                                results.append(l + r)
                            elif char == '-':
                                results.append(l - r)
                            elif char == '*':
                                results.append(l * r)
            return results
        
        return compute(expression)
