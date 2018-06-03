#python
# Generic MODO TD-SDK utils
# Author: Jose Lopez Romo - Zhibade

import lx

def query_user_value(user_value):
    """
    Utility function for querying user values
    """

    return lx.eval("user.value {0} ?".format(user_value))
