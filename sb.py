# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys
from gtts import gTTS
from googletrans import Translator


#client = LineClient()
client = LineClient(id='EMAIL HERE', passwd='PASSWORD HERE')
#client = LineClient(authToken='AUTH TOKEN')
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

poll = LinePoll(client)
mode='self'
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:
#=========================================================================================================================================#
            #if op.type in OpType._VALUES_TO_NAMES:
            #    print("[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type])))
#=========================================================================================================================================#
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
                            elif text.lower() == 'unsend me':
                                client.unsendMessage(msg_id)
                            elif text.lower() == 'speed':
                                start = time.time()
                                client.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                client.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if client.getContact(u).videoProfile != None:
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
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
                            elif text.lower() == 'summon':
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm, jml = [], len(nama)
                                if jml <= 20:
                                    client.mention(receiver, nama)
                                if jml > 20 and jml <= 40:
                                    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, len(nama)):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
                                if jml > 40 and jml <= 60:
                                    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, len(nama)):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
                                if jml > 60 and jml <= 80:
                                    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, len(nama)):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
                                if jml > 80 and jml <= 100:
                                    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, 80):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for m in range(80, len(nama)):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
			        if jml > 100 and jml <= 120:
				    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, 80):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for m in range(80, 100):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(100, len(nama)):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				if jml > 120 and jml <= 140:
				    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, 80):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for m in range(80, 100):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(100, 120):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(120, len(nama)):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				if jml > 140 and jml <= 160:
				    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, 80):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for m in range(80, 100):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(100, 120):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(120, 140):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(140, len(nama)):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
                                client.sendText(receiver, "Members :"+str(jml))
                            elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    client.sendText(receiver, cctv['sidermem'][msg.to])
                                else:
                                    client.sendText(receiver, "Heh belom di Set")
                            elif text.lower() == 'mode:self':
                                mode = 'self'
                                client.sendText(receiver, 'Mode Public Off')
                            elif text.lower() == 'mode:public':
                                mode = 'public'
                                client.sendText(receiver, 'Mode Public ON')
                            elif text.lower() == 'restart':
                                restart_program()
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
            elif mode == 'public' and op.type == 26:
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
                                client.tag(receiver, sender)
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = client.getContact(u).pictureStatus
                                    if client.getContact(u).videoProfile != None:
                                        client.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
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
							elif text.lower() == 'summon':
                                group = client.getGroup(receiver)
                                nama = [contact.mid for contact in group.members]
                                nm, jml = [], len(nama)
                                if jml <= 20:
                                    client.mention(receiver, nama)
                                if jml > 20 and jml <= 40:
                                    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, len(nama)):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
                                if jml > 40 and jml <= 60:
                                    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, len(nama)):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
                                if jml > 60 and jml <= 80:
                                    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, len(nama)):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
                                if jml > 80 and jml <= 100:
                                    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, 80):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for m in range(80, len(nama)):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				if jml > 100 and jml <= 120:
				    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, 80):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for m in range(80, 100):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(100, len(nama)):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				if jml > 120 and jml <= 140:
				    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, 80):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for m in range(80, 100):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(100, 120):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(120, len(nama)):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				if jml > 140 and jml <= 160:
				    for i in range(0, 20):
                                        nm += [nama[i]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for j in range(20, 40):
                                        nm += [nama[j]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for k in range(40, 60):
                                        nm += [nama[k]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for l in range(60, 80):
                                        nm += [nama[l]]
                                    client.mention(receiver, nm)
				    nm = []
                                    for m in range(80, 100):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(100, 120):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(120, 140):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
				    nm = []
				    for m in range(140, len(nama)):
                                        nm += [nama[m]]
                                    client.mention(receiver, nm)
                                client.sendText(receiver, "Members :"+str(jml))
                except Exception as e:
                    client.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = client.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                client.sendText(op.param1, str(random.choice(pref))+' '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        client.log("[SINGLE_TRACE] ERROR : " + str(e))
