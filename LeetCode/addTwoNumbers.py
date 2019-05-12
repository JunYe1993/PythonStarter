from LeetStruct.ListNode import ListNode 

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = n = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            n.next = ListNode((v1 + v2 + carry)%10)
            carry = (v1 + v2 + carry)/10
            n = n.next
        return root.next


