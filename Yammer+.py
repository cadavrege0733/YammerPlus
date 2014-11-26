import yampy

authenticator = yampy.Authenticator(client_id="I4n084DO48GpDvnSGwDkg",
                            client_secret="zvodrbLQ94MxlyUz1gvBtuOw8NcZ7Oqki2qFJ2eITs")
redirect_uri = "http://www.iwillge.com"
auth_url = authenticator.authorization_url(redirect_uri=redirect_uri)
access_token = "PYIasgWU2VyM3KwRPEcOw"
yammer = yampy.Yammer(access_token)


topic_name = input("ENTER TOPIC: ")
#prints dpndrive using search, not ID  number
topic_info = yammer.client.get("/search", search=topic_name,
                        page=1, num_per_page=1)['topics'][0]

print("\nTOPIC: " + topic_name)

topic_id = str(topic_info['id'])
print("ID: " + topic_id)


#gets list of messages with topic "dpndrive"
yamlist = yammer.client.get("/messages/about_topic/" + topic_id,
                            limit=5, threaded="true")

print("\n")

#prints list of messages with sender and timestamp
for yam in yamlist['messages']:
    senderid = yam['sender_id']
    sender = yammer.client.get("/users/" + str(senderid))['full_name']
    print("Sent By: " + str(sender))
    print("Posted at: " + yam['created_at'][:19])
    yamtext = yam['body']['plain']
    print(yamtext.split("\n\ncc: ")[0])
    print("\n")

#print(yammer.client.get("/messages/about_topic/6419232", limit=1))

