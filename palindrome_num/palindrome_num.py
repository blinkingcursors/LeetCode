def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    if x < 10:
        return True
    else:

        original = x
        placeholder = 0
        reversed = 0
        while x >= 1:
            x = int(x)
            placeholder = x % 10
            x = x/10
            reversed = reversed*10 + placeholder

    if reversed == original:
        return True
    else:
        return False


if __name__ == '__main__':
    print(isPalindrome(123))
