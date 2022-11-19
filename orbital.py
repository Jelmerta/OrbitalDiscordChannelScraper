import discum     
import json

bot = discum.Client(token='TOKEN_HERE', log=False)
destinysRoomMemberIds = set()

@bot.gateway.command
def helloworld(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
    
    if not resp.event.voice_state_updated:
        return
    
    m = resp.parsed.auto()
    member_id = m['user_id']
    print("member " + member_id + " with username")
    print(m['member']['user']['username'])
    
    channel_id = m['channel_id'] # either null or the channel id
    print("wants to join channel " + str(channel_id))
#    if (channel_id == '265362793262350338'):
    if (channel_id == '705904180329709578'):# Test room
        print('add')
        destinysRoomMemberIds.add(member_id)
        update_room_members(destinysRoomMemberIds)

    if (channel_id == None and member_id in destinysRoomMemberIds):
        print('remove')
        destinysRoomMemberIds.remove(member_id)
        update_room_members(destinysRoomMemberIds)

    print()

def update_room_members(room_member_ids):
    print("new channel ids: " + str(room_member_ids))
    f = open("/Orbiters/orbiters.txt", "w")
    for member_id in room_member_ids:
        f.write(member_id)
    f.close()

bot.gateway.run(auto_reconnect=True)
