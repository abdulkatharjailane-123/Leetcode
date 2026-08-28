class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next


# Create linked list
def create_list(arr):
    dummy = ListNode(0)
    current = dummy

    for value in arr:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Display linked list
def display(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


# Example
l1 = create_list([2, 4, 3])
l2 = create_list([5, 6, 4])

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

display(result)