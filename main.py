from claude_api import Client
cookie = "sessionKey=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; intercom-device-id-lupk8zyo=94c8d063-e875-4f74-93aa-d846179a171d; cf_clearance=KFIraFxjzzYNIHvYZhii2YRWvDwEhi_hbamDeXCmPvk-1692266549-0-1-7b16060e.8a321f74.2c1759ee-0.2.1692266549; intercom-session-lupk8zyo=eUlyREJJcVZzVSs5bEVQZml5VmVycWNJZEUzRkNHd2JMeGxyR2s0c0tnRmF1bm82WWFMN3k2VklHQlY3TW5SWi0tM05KODFnRnpKbDlyQW92ZkNlNXhadz09--3236333b7d43a7c5160657492bcefcea11745011; __cf_bm=RW0yft_HUKFE0DbAg.cnAChZ_qRHmaKdWAHSOjpX9To-1692267627-0-AQr9INBkb1gBmf45dIgAGzxpigpTFis3T2Rjfv29B+XMKF5CyRgw3mpEQV/qWdNUqyR7x/HEF6giWGMQSfbpw7M="
claude_api = Client(cookie)

conversations = claude_api.list_all_conversations()
# for conversation in conversations:
#     conversation_id = conversation['uuid']
#     print(conversation_id)

prompt = "Hello, Claude!"
conversation_id = claude_api.create_new_chat()['uuid']

print(conversation_id)
response = claude_api.send_message(prompt,conversation_id)
print(response)