# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys
from gtts import gTTS
from googletrans import Translator


client = LineClient()
#client = LineClient(id='EMAIL HERE', passwd='PASSWORD HERE')
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

def siderMembers(to, mid):
    	try:
        	arrData = ""
		textx = "Haii "
		arr = []
		no = 1
		num = 2
		for i in mid:
			mention = "@x\n"
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention+wait["mention"]
			if no < len(mid):
				no += 1
				textx += "%i. " % (num)
				num=(num+1)
			else:
				try:
			    		no = "\n┗━━[ {} ]".format(str(client.getGroup(to).name))
				except:
				    	no = "\n┗━━[ Success ]"
		client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
        	client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

while True:
	try:
		ops=poll.singleTrace(count=50)
		if ops != None:
			for op in ops:
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
									nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
									if jml <= 20:
										client.mention(receiver, nama)
									if jml > 20 and jml <= 40:
										for i in range(0, 20):
											nm1 += [nama[i]]
										client.mention(receiver, nm1)
										for j in range(20, len(nama)):
											nm2 += [nama[j]]
										client.mention(receiver, nm2)
									if jml > 40 and jml <= 60:
										for i in range(0, 20):
											nm1 += [nama[i]]
										client.mention(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										client.mention(receiver, nm2)
										for k in range(40, len(nama)):
											nm3 += [nama[k]]
										client.mention(receiver, nm3)
									if jml > 60 and jml <= 80:
										for i in range(0, 20):
											nm1 += [nama[i]]
										client.mention(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										client.mention(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										client.mention(receiver, nm3)
										for l in range(60, len(nama)):
											nm4 += [nama[l]]
										client.mention(receiver, nm4)
									if jml > 80 and jml <= 100:
										for i in range(0, 20):
											nm1 += [nama[i]]
										client.mention(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										client.mention(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										client.mention(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										client.mention(receiver, nm4)
										for m in range(80, len(nama)):
											nm5 += [nama[m]]
										client.mention(receiver, nm5)
									client.sendText(receiver, "Members :"+str(jml))
								elif text.lower() == 'sider on':
									try:
										del cctv['point'][receiver]
										del cctv['sidermem'][receiver]
										del cctv['cyduk'][receiver]
									except:
										pass
									cctv['point'][receiver] = msg.id
									cctv['sidermem'][receiver] = ""
									cctv['cyduk'][receiver]=True
								elif text.lower() == 'sider off':
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
									nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
									if jml <= 20:
										client.mention(receiver, nama)
									if jml > 20 and jml <= 40:
										for i in range(0, 20):
											nm1 += [nama[i]]
										client.mention(receiver, nm1)
										for j in range(20, len(nama)):
											nm2 += [nama[j]]
										client.mention(receiver, nm2)
									if jml > 40 and jml <= 60:
										for i in range(0, 20):
											nm1 += [nama[i]]
										client.mention(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										client.mention(receiver, nm2)
										for k in range(40, len(nama)):
											nm3 += [nama[k]]
										client.mention(receiver, nm3)
									if jml > 60 and jml <= 80:
										for i in range(0, 20):
											nm1 += [nama[i]]
										client.mention(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										client.mention(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										client.mention(receiver, nm3)
										for l in range(60, len(nama)):
											nm4 += [nama[l]]
										client.mention(receiver, nm4)
									if jml > 80 and jml <= 100:
										for i in range(0, 20):
											nm1 += [nama[i]]
										client.mention(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										client.mention(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										client.mention(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										client.mention(receiver, nm4)
										for m in range(80, len(nama)):
											nm5 += [nama[m]]
										client.mention(receiver, nm5)
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
									siderMembers(op.param1, [op.param2])
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
