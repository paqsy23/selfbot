# -*- coding: utf-8 -*-
from linepy import *
import json, time, random

client = LineClient()
#client = LineClient(authToken='AUTH TOKEN')
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(client)

cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

while True:
    try:
        ops=poll.singleTrace(count=50)
        for op in ops:
            if op.type == 26:
                msg = op.message
                if msg.text != None:
                    if msg.toType == 2:
                        may = client.getProfile().mid
                        if may in str(msg.contentMetadata) and 'MENTION' in str(msg.contentMetadata):
                            client.sendText(msg.to, str('apa ??'))
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            if op.type == 25:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            client.sendChatChecked(receiver, msg_id)
                            contact = client.getContact(sender)
                            if text.lower() == 'me':
                                client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            #elif text.lower() == 'speed':
                                #start = time.time()
                                #client.sendText(receiver, "TestSpeed")
                                #elapsed_time = time.time() - start
                                #client.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    client.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    client.sendText(receiver, str(e))
                            elif text.lower() == 'tagall':
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                                if jml <= 20:
                                    client.mention(receiver, nama)
                                if jml > 20 and jml <= 40:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(21, len(nama)):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                if jml > 40 and jml <= 60:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(41, len(nama)):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                if jml > 60 and jml <= 80:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(61, len(nama)):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                if jml > 80 and jml <= 100:
                                    for i in range(0, 20):
                                        nm1 += [nama[i]]
                                    client.mention(receiver, nm1)
                                    for j in range(21, 40):
                                        nm2 += [nama[j]]
                                    client.mention(receiver, nm2)
                                    for k in range(41, 60):
                                        nm3 += [nama[k]]
                                    client.mention(receiver, nm3)
                                    for l in range(61, 80):
                                        nm4 += [nama[l]]
                                    client.mention(receiver, nm4)
                                    for m in range(81, len(nama)):
                                        nm5 += [nama[m]]
                                    client.mention(receiver, nm5)             
                                client.sendText(receiver, "Members :"+str(jml))
                            elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][msg.to]
                                    del cctv['sidermem'][msg.to]
                                    del cctv['cyduk'][msg.to]
                                except:
                                    pass
                                cctv['point'][msg.to] = msg.id
                                cctv['sidermem'][msg.to] = ""
                                cctv['cyduk'][msg.to]=True
                            elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][msg.to]=False
                                    client.sendText(msg.to, cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(msg.to, "Heh belom di Set")
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))

            elif op.type == OpType.NOTIFIED_READ_MESSAGE:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                client.sendText(op.param1, str(random.choice(pref))+' @'+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass

            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
