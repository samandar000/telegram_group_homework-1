from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    users_msgs = {}
    for i in users_id:
        users_msgs[i] = 0
    
    for msg in data['messages']:
        id = msg.get('from_id',False)
        
        if id:
            users_msgs[id] += 1
        id = msg.get('actor_id', False)
        if id and id in users_id:
            users_msgs[id] += 1
        
    return users_msgs
    
data = read_data('data/result.json')
ids = find_all_users_id(data)
