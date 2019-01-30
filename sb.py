# -*- coding: utf-8 -*-
from linepy import *
import json, time, random, tempfile, os, sys, pytz, requests, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
from datetime import timedelta, date
from datetime import datetime


client = LineClient()
client.log("Auth Token : " + str(client.authToken))
channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))

paq = LineClient(id='paqsy23@gmail.com', passwd='rengginang23')
#paq = LineClient()
paq.log("Auth Token : " + str(paq.authToken))
channel1 = LineChannel(paq)
paq.log("Channel Access Token : " + str(channel1.channelAccessToken))

poll = LinePoll(client)
cctv={
	"cyduk":{},
	"point":{},
	"sidermem":{}
}

limit = 1
welcome = []
mid = client.getProfile().mid
Amid = paq.getProfile().mid
Bots = [mid, Amid]

def help():
	helpMessage = " [ Help ]" + "\n" + \
		"➣ Help\n" + \
		"➣ Me\n" + \
		"➣ Mymid\n" + \
		"➣ Babay \n" + \
		"➣ Mid「@」\n" + \
		"➣ Info 「@」\n" + \
		"➣ Cancelall \n" + \
		"➣ Speed\n" + \
		"➣ Summon\n" + \
		"➣ Siders「on/off」\n" + \
		"➣ Welcome「on/off」\n"
	return helpMessage

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

def leaveMembers(to, mid):
	try:
		arrData = ""
		textx = "Yahh, si "
		arr = []
		for i in mid:
			mention = "@paq23 "
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention + "baper :("
		paq.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		paq.sendMessage(to, "[ INFO ] Error :\n" + str(error))
	
def welcomeMembers(to, mid):
	try:
		arrData = ""
		textx = "Haii  "
		arr = []
		ginfo = client.getGroup(to)
		for i in mid:
			mention = "@paq23\n"
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention+"Selamat datang di group "+str(ginfo.name)+"\nJangan lupa follow ig @paqsy23 yaa\nAuto follback kok"
		paq.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		paq.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
	try:
		arrData = ""
		textx = "Total Mention User「{}」\n\n  [ Mention ]\n❂➣ ".format(str(len(mid)))
		arr = []
		no = 1
		num = 2
		for i in mid:
			mention = "@paq23\n"
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention
			if no < len(mid):
				no += 1
				textx += "❂➣ "
			else:
				pass
		paq.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		paq.sendMessage(to, "[ INFO ] Error :\n" + str(error))
	
def siderMembers(to, mid):
	try:
		arrData = ""
		textx = "Haii kak "
		arr = []
		for i in mid:
			mention = "@paq23\n"
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention + "Ikut nimbrung gih"
		paq.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		paq.sendMessage(to, "[ INFO ] Error :\n" + str(error))

while True:
	try:
		ops=poll.singleTrace(count=50)
		if ops != None:
			for op in ops:
				if op.type == 15:
					if op.param1 in welcome:
						leaveMembers(op.param1, [op.param2])
				if op.type == 17:
					if op.param1 in welcome:
						welcomeMembers(op.param1, [op.param2])
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
									paq.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
								elif text.lower() == 'join bot':
									group = client.getGroup(receiver)
									nama = [contact.mid for contact in group.members]
									if Amid not in nama:
										client.inviteIntoGroup(msg.to,[Amid])
										paq.acceptGroupInvitation(msg.to)
										paq.sendMessage(msg.to,"Bot already on!")
									else:
										paq.sendMessage(msg.to,"Bot lu disini goblog!")
								elif text.lower() == 'babay':
									group = paq.getGroup(receiver)
									paq.sendMessage(msg.to, "Bye, grup " + str(group.name))
									paq.leaveGroup(msg.to)
								elif text.lower() == "respon":
									paq.sendMessage(msg.to,"Hadir!")
								elif text.lower() == "help":
									helpMessage = help()
									paq.sendMessage(msg.to, str(helpMessage))
								elif text.lower() == "mymid":
									paq.sendMessage(msg.to, msg._from)
								elif "info " in msg.text.lower():
									key = eval(msg.contentMetadata["MENTION"])
									key1 = key["MENTIONEES"][0]["M"]
									mi = client.getContact(key1)
									paq.sendMessage(msg.to, "➣ Nama : "+str(mi.displayName)+"\n➣ Mid : " +key1+"\n➣ Status : "+str(mi.statusMessage))
									paq.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
								elif 'mid ' in msg.text.lower():
									key = eval(msg.contentMetadata["MENTION"])
									key1 = key["MENTIONEES"][0]["M"]
									mi = client.getContact(key1)
									paq.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
									paq.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
								elif text.lower() == 'spam':
									korban = msg.text.lower().replace('spam: ','')
									jumlah = int(korban)
									if jumlah <= 1000:
										for var in range(0,jumlah):
											paq.sendMessage(msg.to, "BACOD")
								elif 'spampc: ' in msg.text.lower():
									korban = msg.text.lower().replace('spam: ','')
									korban2 = korban.split(' ')
									midd = korban2[0]
									jumlah = int(korban2[1])
									if jumlah <= 1000:
										for var in range(0,jumlah):
											client.sendMessage(midd, "spam")
								elif "kick " in msg.text.lower():
									key = eval(msg.contentMetadata["MENTION"])
									key["MENTIONEES"][0]["M"]
									targets = []
									for x in key["MENTIONEES"]:
										targets.append(x["M"])
										for target in targets:
											try:
												paq.kickoutFromGroup(msg.to, [target])
											except:
												pass
								elif text.lower() == "cancelall":
									group = client.getGroup(receiver)
									pending = [contact.mid for contact in group.invitee]
									for mid in pending:
										paq.cancelGroupInvitation(msg.to, [mid])
								elif text.lower() == "clear":
									group = client.getGroup(receiver)
									nama = [contact.mid for contact in group.members]
									pending = [contact.mid for contact in group.invitee]
									botid = paq.getProfile().mid
									myid = client.getProfile().mid
									nama.remove(myid)
									i = int(0)
									while nama is not None:
										try:
											paq.kickoutFromGroup(msg.to, [nama[i]])
											i += 1
										except:
											client.inviteIntoGroup(msg.to,[Amid])
											paq.acceptGroupInvitation(msg.to)
											i = 0
									for mid in pending:
										client.cancelGroupInvitation(msg.to, [mid])
								elif text.lower() == 'speed':
									start = time.time()
									client.sendText(receiver, "TestSpeed")
									elapsed_time = time.time() - start
									client.sendText(receiver, "%s detik" % (elapsed_time))
								elif text.lower() == 'tagall':
									group = client.getGroup(receiver)
									nama = [contact.mid for contact in group.members]
									nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, nm10, jml = [], [], [], [], [], [], [], [], [], [], len(nama)
									if jml <= 20:
										mentionMembers(receiver, nama)
									if jml > 20 and jml <= 40:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, len(nama)):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
									if jml > 40 and jml <= 60:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, len(nama)):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
									if jml > 60 and jml <= 80:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, len(nama)):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
									if jml > 80 and jml <= 100:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, len(nama)):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
									if jml > 100 and jml <= 120:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, len(nama)):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
									if jml > 120 and jml <= 140:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, 120):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
										for o in range(120, len(nama)):
											nm7 += [nama[o]]
										mentionMembers(receiver, nm7)
									if jml > 140 and jml <= 160:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, 120):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
										for o in range(120, 140):
											nm7 += [nama[o]]
										mentionMembers(receiver, nm7)
										for p in range(140, len(nama)):
											nm8 += [nama[p]]
										mentionMembers(receiver, nm8)
									if jml > 160 and jml <= 180:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, 120):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
										for o in range(120, 140):
											nm7 += [nama[o]]
										mentionMembers(receiver, nm7)
										for p in range(140, 160):
											nm8 += [nama[p]]
										mentionMembers(receiver, nm8)
										for q in range(160, len(nama)):
											nm9 += [nama[q]]
										mentionMembers(receiver, nm9)
									if jml > 180 and jml <= 200:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, 120):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
										for o in range(120, 140):
											nm7 += [nama[o]]
										mentionMembers(receiver, nm7)
										for p in range(140, 160):
											nm8 += [nama[p]]
										mentionMembers(receiver, nm8)
										for q in range(160, 180):
											nm9 += [nama[q]]
										mentionMembers(receiver, nm9)
										for r in range(180, len(nama)):
											nm10 += [nama[r]]
										mentionMembers(receiver, nm10)
								elif text.lower() == 'siders on':
									try:
										tz = pytz.timezone("Asia/Jakarta")
										timeNow = datetime.now(tz=tz)
										client.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
										del cctv['point'][receiver]
										del cctv['sidermem'][receiver]
										del cctv['cyduk'][receiver]
									except:
										pass
									cctv['point'][receiver] = msg.id
									cctv['sidermem'][receiver] = ""
									cctv['cyduk'][receiver]=True
								elif text.lower() == 'siders off':
									if msg.to in cctv['point']:
										cctv['cyduk'][receiver]=False
										tz = pytz.timezone("Asia/Jakarta")
										timeNow = datetime.now(tz=tz)
										client.sendText(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
									else:
										client.sendText(msg.to, "Cek sider sudah nonaktif")
								elif text.lower() == 'restart':
									restart_program()
								elif 'welcome ' in msg.text.lower():
									spl = msg.text.lower().replace('welcome ','')
									msgs = ""
									if spl == 'on':
										if msg.to in welcome:
											msgs = "Welcome Msg sudah aktif"
										else:
											welcome.append(msg.to)
											ginfo = client.getGroup(msg.to)
											msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
										client.sendMessage(msg.to, msgs)
									elif spl == 'off':
										if msg.to in welcome:
											welcome.remove(msg.to)
											ginfo = client.getGroup(msg.to)
											msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
										else:
											msgs = "Welcome Msg sudah tidak aktif"
										client.sendMessage(msg.to, msgs)
					except Exception as e:
						client.log("[SEND_MESSAGE] ERROR : " + str(e))
	#=========================================================================================================================================#
				elif op.type == 26:
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
									paq.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
								elif ' bot ' in text.lower() or ' bot' in text.lower():
									paq.sendMessage(msg.to, "Apaan njir!")
								elif text.lower() == 'babay':
									group = paq.getGroup(receiver)
									paq.sendMessage(msg.to, "Bye, grup " + str(group.name))
									paq.leaveGroup(msg.to)
								elif text.lower() == "respon":
									paq.sendMessage(msg.to,"Hadir!")
								elif text.lower() == "help":
									helpMessage = help()
									paq.sendMessage(msg.to, str(helpMessage))
								elif text.lower() == "mymid":
									paq.sendMessage(msg.to, msg._from)
								elif "info " in msg.text.lower():
									key = eval(msg.contentMetadata["MENTION"])
									key1 = key["MENTIONEES"][0]["M"]
									mi = client.getContact(key1)
									paq.sendMessage(msg.to, "➣ Nama : "+str(mi.displayName)+"\n➣ Mid : " +key1+"\n➣ Status : "+str(mi.statusMessage))
									paq.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
								elif 'mid ' in msg.text.lower():
									key = eval(msg.contentMetadata["MENTION"])
									key1 = key["MENTIONEES"][0]["M"]
									mi = client.getContact(key1)
									paq.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
									paq.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
								elif text.lower() == 'spam':
									korban = msg.text.lower().replace('spam: ','')
									jumlah = int(korban)
									if jumlah <= 1000:
										for var in range(0,jumlah):
											paq.sendMessage(msg.to, "BACOD")
								elif text.lower() == 'tagall':
									group = client.getGroup(receiver)
									nama = [contact.mid for contact in group.members]
									nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, nm10, jml = [], [], [], [], [], [], [], [], [], [], len(nama)
									if jml <= 20:
										mentionMembers(receiver, nama)
									if jml > 20 and jml <= 40:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, len(nama)):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
									if jml > 40 and jml <= 60:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, len(nama)):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
									if jml > 60 and jml <= 80:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, len(nama)):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
									if jml > 80 and jml <= 100:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, len(nama)):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
									if jml > 100 and jml <= 120:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, len(nama)):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
									if jml > 120 and jml <= 140:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, 120):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
										for o in range(120, len(nama)):
											nm7 += [nama[o]]
										mentionMembers(receiver, nm7)
									if jml > 140 and jml <= 160:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, 120):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
										for o in range(120, 140):
											nm7 += [nama[o]]
										mentionMembers(receiver, nm7)
										for p in range(140, len(nama)):
											nm8 += [nama[p]]
										mentionMembers(receiver, nm8)
									if jml > 160 and jml <= 180:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, 120):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
										for o in range(120, 140):
											nm7 += [nama[o]]
										mentionMembers(receiver, nm7)
										for p in range(140, 160):
											nm8 += [nama[p]]
										mentionMembers(receiver, nm8)
										for q in range(160, len(nama)):
											nm9 += [nama[q]]
										mentionMembers(receiver, nm9)
									if jml > 180 and jml <= 200:
										for i in range(0, 20):
											nm1 += [nama[i]]
										mentionMembers(receiver, nm1)
										for j in range(20, 40):
											nm2 += [nama[j]]
										mentionMembers(receiver, nm2)
										for k in range(40, 60):
											nm3 += [nama[k]]
										mentionMembers(receiver, nm3)
										for l in range(60, 80):
											nm4 += [nama[l]]
										mentionMembers(receiver, nm4)
										for m in range(80, 100):
											nm5 += [nama[m]]
										mentionMembers(receiver, nm5)
										for n in range(100, 120):
											nm6 += [nama[n]]
										mentionMembers(receiver, nm6)
										for o in range(120, 140):
											nm7 += [nama[o]]
										mentionMembers(receiver, nm7)
										for p in range(140, 160):
											nm8 += [nama[p]]
										mentionMembers(receiver, nm8)
										for q in range(160, 180):
											nm9 += [nama[q]]
										mentionMembers(receiver, nm9)
										for r in range(180, len(nama)):
											nm10 += [nama[r]]
										mentionMembers(receiver, nm10)
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
