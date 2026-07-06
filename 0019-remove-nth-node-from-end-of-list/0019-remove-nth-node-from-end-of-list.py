# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        if count == n:
            return head.next

        curr = head
        cou = 1

        while cou < count - n:
            curr = curr.next
            cou += 1

        curr.next = curr.next.next

        return head