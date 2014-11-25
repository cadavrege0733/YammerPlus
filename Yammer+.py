import yampy

authenticator = yampy.Authenticator(client_id="I4n084DO48GpDvnSGwDkg",
                                    client_secret="zvodrbLQ94MxlyUz1gvBtuOw8NcZ7Oqki2qFJ2eITs")
redirect_uri = "http://www.iwillge.com"
auth_url = authenticator.authorization_url(redirect_uri=redirect_uri)
access_token = "PYIasgWU2VyM3KwRPEcOw"
yammer = yampy.Yammer(access_token)

yamlist = yammer.client.get("/messages/about_topic/6419232", limit=10)

print("TOPIC: " + yamlist['references'][0]['name'])
print("\n")

for yam in yamlist['messages']:
    senderid = yam['sender_id']
    sender = yammer.client.get("/users/" + str(senderid))['full_name']
    print("Sent By: " + str(sender))
    print("Posted at: " + yam['created_at'][:19])
    print(yam['body']['plain'])
    print("\n")

#print(yammer.client.get("/messages/about_topic/6419232", limit=1))
