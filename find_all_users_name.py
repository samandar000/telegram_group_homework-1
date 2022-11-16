from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    user = []
    for i in data['messages']:
        if i.get("actor") and i.get('actor') not in user:
            user.append(i['actor'] )
        if i.get('from') and i.get('from') not in user:
            user.append(i['from'])
        
    return user


