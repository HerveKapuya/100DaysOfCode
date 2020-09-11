
import array as arr

Item = arr.array('i',[3,9,8,4,1,4,1])

# Defining our Function named ItemDuplicate

def ItemDuplicate (Item) :

    # Verification doublons

       if len(Item) == len(set(Item)) :
           return False
       else:
           return True

# Declaring our list

result = ItemDuplicate(Item)

if result:

    print('Yes, there is some Duplicate Item')
else:
    print('Nothing Duplicate Item inside')
