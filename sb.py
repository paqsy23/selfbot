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

poll = LinePoll(client)
cctv={
	"cyduk":{},
	"point":{},
	"sidermem":{}
}

autoRead = False
protectkick = []
welcome = []
mid = client.getProfile().mid
oaMid = "u1ffd94edbb783a0bd35dfd83d6f7193e"

def help():
	helpMessage = " [ Help ]" + "\n" + \
		"➣ Me\n" + \
		"➣ Mymid\n" + \
		"➣ Mid「@」\n" + \
		"➣ Info 「@」\n" + \
		"➣ Cancelall \n" + \
		"➣ Tagall\n" + \
		"➣ Sider「on/off」\n" + \
		"➣ ProtectKick「on/off」\n" + \
		"➣ AutoRead「on/off」\n" + \
		"➣ Welcome「on/off」"
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
			mention = "@kimak "
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention + "baper :("
		client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		client.sendMessage(to, "[ INFO ] Error :\n" + str(error))
	
def welcomeMembers(to, mid):
	try:
		arrData = ""
		textx = "Haii  "
		arr = []
		ginfo = client.getGroup(to)
		for i in mid:
			mention = "@kimak\n"
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention+"Selamat datang di group "+str(ginfo.name)+"\nJangan lupa follow ig @paqsy23 yaa\nAuto follback kok"
		client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
	try:
		arrData = ""
		textx = "Total Mention User「{}」\n\n  [ Mention ]\n❂➣ ".format(str(len(mid)))
		arr = []
		no = 1
		num = 2
		for i in mid:
			mention = "@kimak\n"
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
		client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		client.sendMessage(to, "[ INFO ] Error :\n" + str(error))
	
def siderMembers(to, mid):
	try:
		arrData = ""
		textx = "Haii "
		arr = []
		for i in mid:
			mention = "@kimak\n"
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention + "Ikut nimbrung gih"
		client.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		client.sendMessage(to, "[ INFO ] Error :\n" + str(error))

while True:
	try:
		ops=poll.singleTrace(count=50)
		if ops != None:
			for op in ops:
				if op.type == 19:
					if op.param1 in protectkick:
						try:
							client.kickoutFromGroup(op.param1,[op.param2])
						except:
							pass
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
						if msg.contentType == 13:
							try:
								contact = client.getContact(msg.contentMetadata["mid"])
								ret_ = "[ Details Contact ]"
								ret_ += "\nNama : {}".format(str(contact.displayName))
								ret_ += "\nMID : {}".format(str(msg.contentMetadata["mid"]))
								ret_ += "\nBio : {}".format(str(contact.statusMessage))
								client.sendMessage(msg.to, str(ret_))
							except:
								client.sendMessage(msg.to, "Kontak tidak valid")
						elif msg.contentType == 0:
							if autoRead == True:
								client.sendChatChecked(msg.to,msg.id)
							if msg.toType == 2:
								contact = client.getContact(sender)
								if text.lower() == 'me':
									client.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
									client.sendMessage(receiver, None, contentMetadata={'mid': oaMid}, contentType=13)
								elif text.lower() == "help":
									helpMessage = help()
									client.sendMessage(msg.to, str(helpMessage))
								elif text.lower() == "protectkick on":
									spl = msg.text.replace('Protectkick ','')
									if spl == 'on':
										if msg.to in protectkick:
											msgs = "Protect kick sudah aktif"
										else:
											protectkick.append(msg.to)
											ginfo = client.getGroup(msg.to)
											msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
										client.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
									elif spl == 'off':
										if msg.to in protectkick:
											protectkick.remove(msg.to)
											ginfo = client.getGroup(msg.to)
											msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
										else:
											msgs = "Protect kick sudah tidak aktif"
										client.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
								elif text.lower() == "autoread on":
									if autoRead == True:
										client.sendMessage(msg.to,"Auto read is already on")
									else:
										client.sendMessage(msg.to,"Auto read on")
										autoRead = True
								elif text.lower() == "autoread off":
									if autoRead == False:
										client.sendMessage(msg.to,"Auto read is already off")
									else:
										client.sendMessage(msg.to,"Auto read off")
										autoRead = False
								elif text.lower() == "mymid":
									client.sendMessage(msg.to, msg._from)
								elif "info " in msg.text.lower():
									key = eval(msg.contentMetadata["MENTION"])
									key1 = key["MENTIONEES"][0]["M"]
									mi = client.getContact(key1)
									client.sendMessage(msg.to, "➣ Nama : "+str(mi.displayName)+"\n➣ Mid : " +key1+"\n➣ Status : "+str(mi.statusMessage))
									client.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
								elif 'mid ' in msg.text.lower():
									key = eval(msg.contentMetadata["MENTION"])
									key1 = key["MENTIONEES"][0]["M"]
									mi = client.getContact(key1)
									client.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
									client.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
								elif "kick " in msg.text.lower():
									key = eval(msg.contentMetadata["MENTION"])
									key["MENTIONEES"][0]["M"]
									targets = []
									for x in key["MENTIONEES"]:
										targets.append(x["M"])
										for target in targets:
											try:
												client.kickoutFromGroup(msg.to, [target])
											except:
												pass
								elif text.lower() == "cancelall":
									group = client.getGroup(receiver)
									pending = [contact.mid for contact in group.invitee]
									for mid in pending:
										client.cancelGroupInvitation(msg.to, [mid])
								elif text.lower() == "clear":
									client.sendMessage(msg.to, None, contentMetadata={'mid': oaMid}, contentType=13)
									client.sendMessage(msg.to, "Di Add ye :v")
									group = client.getGroup(receiver)
									nama = [contact.mid for contact in group.members]
									pending = [contact.mid for contact in group.invitee]
									nama.remove(mid)
									for i in nama:
										try:
											client.kickoutFromGroup(msg.to, [i])
										except:
											pass
									for i in pending:
										client.cancelGroupInvitation(msg.to, [i])
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
								elif text.lower() == 'sider on':
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
								elif text.lower() == 'sider off':
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
