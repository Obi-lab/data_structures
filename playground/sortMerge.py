class SortMerge():
    
    def main(self,list_one,list_two,m,n):
        #list_one is a array 
        #list_two is an array
        # m is the size of array list_one and n the size of array list_two
        new_list=list_one+list_two
        new_list.sort()
        print(new_list)
        
        
class SortMergeTwo():
    
    def main(self,list_one,list_two,m,n):
        #list_one is a array 
        #list_two is an array
        
        new_list=list_one+list_two
        new_list.sort()
        list_one=[]
        list_one=new_list[len(new_list)-(m+n):]
        print(list_one)
            
# list_one=[1,7,6]
# list_two=[5,8,2]

# #create object of class sortMerge
# sorted=SortMerge()
# sorted.main(list_one,list_two,len(list_one),len(list_two))

list_one=[1,7,6,0,0]
list_two=[5,8,2]

#create object of class sortMerge
sorted=SortMergeTwo()
sorted.main(list_one,list_two,3,len(list_two))


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #concatenate the lists
        new_list=nums1+nums2
        #sort in ascending
        new_list.sort()
        new_list=new_list[len(new_list)-(m+n):]
        print(new_list)

        for i in range(len(nums1)):
            nums1[i]=new_list[i]
        