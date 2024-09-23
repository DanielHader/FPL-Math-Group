
# this function asks a user for an input integer
# min_value and max_value limit the allowed bounds for this number
# if min_value is none then there is no minimum value requirement, likewise for max_value
# it will constantly ask the user for a new value if they provide an invalid one
def handle_input(input_msg, min_value=None, max_value=None):

    # ensure min value and max value make sense
    if (min_value is not None) and (max_value is not None) and (min_value > max_value):
        raise ValueError('min_value must be less than or equal to max_value')

    # choose an appropriate error message for the given bounds
    if min_value == 0 and max_value is None:
        err_string = 'please enter a non-negative integer'
    elif min_value == 1 and max_value is None:
        err_string = 'please enter a positive integer'
    elif min_value is None and max_value is None:
        err_string = 'please enter an integer'
    elif min_value is None:
        err_string = f'please enter an integer no greater than {max_value}'
    elif max_value is None:
        err_string = f'please enter an integer no less than {min_value}'
    else:
        err_string = f'please enter an integer between {min_value} and {max_value} inclusively'

    # constantly ask for an input value until a valid integer is provided
    while True:

        # get the user input as a string
        input_str = input(input_msg)

        # try to convert the input to an int
        try:
            val = int(input_str)
        except:
            # if the value cannot be interpreted as an integer, print error message and try again
            print(err_string)
            continue

        # if value does not meet minimum bound, try again
        if min_value is not None and val < min_value:
            print(err_string)
            continue

        # if value does not meet maximum bound, try again
        if max_value is not None and val > max_value:
            print(err_string)
            continue

        # if we make it this far, we can return the value
        return val

print('''In this demonstration, you and a friend will use the diffie-hellman key exchange protocol for agreeing on a shared, secret number even though you communicate over an open channel. In our case the open channel will involve announcing numbers out loud so that others in the room can hear what you say.

The numbers used in this key exchange will actually represent elements from a finite cyclic group -- that is, the natural numbers taken modulo some number called the "order" of the group.

The first step in this process then is to agree on what order to use for your group. This does not need to be a secret, but ideally it should be a large positive integer. Agree on a large positive number by talking out loud with your friend and then enter it here.
''')

group_order = handle_input('group order = ', min_value=1, max_value=None)

print(f'''
Now you and your friend must agree on a common element from the group which we will call "g", agree with your friend on a value for "g" between 0 and {group_order - 1} inclusively by discussing out loud and enter it here.
''')

g = handle_input('g = ', min_value = 0, max_value=group_order-1)

print(f'''
Now choose a secret number "n" between 1 and {group_order-1}, DO NOT ANNOUNCE IT, which you will multiply g by. This should ideally be large to avoid people guessing it
''')

n = handle_input('n = ', min_value=1, max_value=group_order-1)

ng = (n * g) % group_order

print(f'''
Now we compute the value of n x g, or g added to itself n times. This type of multiplication is simple, but the inverse operation can be very difficult if the numbers are well chosen. Remember this is modular multiplication so the answer will be between {0} and {group_order-1}.

In our case we find that n x g = {n} x {g} = {ng}

Share this number aloud so that your friend knows what it is, and have your friend share their product with you aloud and enter their number, which we will call m*g, here.
''')

mg = handle_input('m*g = ', min_value=0, max_value=group_order-1)

print(f'''
Now you know the value of your chosen n as well as the product of m and g. You can now find the value of n*m*g by simple multiplication and likewise your friend can do likewise. Your shared secret number is:

SHARED SECRET NUMBER = {n * mg % group_order}

This shared number can be used, for instance, as a cipher to encrypt some message. Now discuss why using a finite cyclic group might not be the best choice for this sort of key exchange
''')
