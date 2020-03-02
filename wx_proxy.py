# -*- coding: utf-8 -*-
import os
import operator
import logging
import queue

from flask import Flask
from flask import request
from flask import jsonify

from random import choice
import random
import requests
from datetime import datetime
import json
import time

from const import *

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
wexin_cmd_queue = queue.Queue(maxsize=100)
cnt = 1    
def init_getContact():
    if contract_init() == 1:
        send_dict = {"api":"getContact","sendId":"","option":{"flag":2}}
        wexin_cmd_queue.put(send_dict)
    
#-------------------------------------------------------------------------------------------
def writelog(fpath, data):
    f = open(fpath,'a+',encoding='utf-8')
    f.write(data)
    f.write('\n\n')
    f.close()

#-------------------------------------------------------------------------------------------
@app.route('/admin', methods=['GET'])
def hello_world():
    return 'Hello dear!!'
    
#-------------------------------------------------------------------------------------------    
def process_pic_msg_data(msg_data):
    if get_msg_sender(msg_data) == "管理员":
        return
    room_name = get_room_name(msg_data)
    task_id = get_user_task(room_name)
    value = "1"
    FileDir = DATA_DIR + "\\" + task_id + "\\" + room_name + "\\"
    mkdir(FileDir)
    target_file = save_pic_file(FileDir, get_object_dir(msg_data))
    
    ######################## blockchain ###############################
    json_data = {'taskid_userid': task_id + room_name, 'message': target_file}
    r = user_to_blockchain(json_data)
    Hash = json.loads(r.text).get('Hash')
    ###################################################################
    #json_data = {'action': "user_to_proxy", 'value': value, 'task_id': task_id, 'room_name': room_name, 'message': FileDir+msg['FileName'], 'Hash': Hash}
    reply_msg = ('您的信息已被记录 http://39.99.224.190/share/' + task_id + "/" + room_name + "/" + target_file + '\n区块链hash:' + Hash)
    #user_to_proxy(json_data)
       #http://localhost/share/2020-02-24/19487307280%40chatroom/
       #http://39.99.224.190/2020-02-24/19487307280@chatroom/C:\Users\Public\nfs\data\langan\2020-02-24\19487307280@chatroom\1484ec68e1f4c18966e9a595583af1aa.jpg
    return reply_msg, get_room_wxid(msg_data) 

#-------------------------------------------------------------------------------------------    
def process_video_msg_data(msg_data):
    if get_msg_sender(msg_data) == "管理员":
        return
    room_name = get_room_name(msg_data)
    task_id = get_user_task(room_name)
    value = "1"
    FileDir = DATA_DIR + "\\" + task_id + "\\" + room_name + "\\"
    mkdir(FileDir)
    target_file = save_video_file(FileDir, get_object_dir(msg_data))
    
    ######################## blockchain ###############################
    json_data = {'taskid_userid': task_id + room_name, 'message': target_file}
    r = user_to_blockchain(json_data)
    Hash = json.loads(r.text).get('Hash')
    ###################################################################
    #json_data = {'action': "user_to_proxy", 'value': value, 'task_id': task_id, 'room_name': room_name, 'message': FileDir+msg['FileName'], 'Hash': Hash}
    reply_msg = ('您的信息已被记录 http://39.99.224.190/share/' + task_id + "/" + room_name + "/" + target_file + '\n区块链hash:' + Hash)
    #user_to_proxy(json_data)
       #http://localhost/share/2020-02-24/19487307280%40chatroom/
       #http://39.99.224.190/2020-02-24/19487307280@chatroom/C:\Users\Public\nfs\data\langan\2020-02-24\19487307280@chatroom\1484ec68e1f4c18966e9a595583af1aa.jpg
    return reply_msg, get_room_wxid(msg_data) 
    
def process_voice_msg_data(msg_data):
    if get_msg_sender(msg_data) == "管理员":
        return
    room_name = get_room_name(msg_data)
    task_id = get_user_task(room_name)
    value = "1"
    FileDir = DATA_DIR + "\\" + task_id + "\\" + room_name + "\\"
    mkdir(FileDir)
    target_file = save_voice_file(FileDir, get_object_dir(msg_data))
    
    ######################## blockchain ###############################
    json_data = {'taskid_userid': task_id + room_name, 'message': target_file}
    r = user_to_blockchain(json_data)
    Hash = json.loads(r.text).get('Hash')
    ###################################################################
    #json_data = {'action': "user_to_proxy", 'value': value, 'task_id': task_id, 'room_name': room_name, 'message': FileDir+msg['FileName'], 'Hash': Hash}
    reply_msg = ('您的信息已被记录 http://39.99.224.190/share/' + task_id + "/" + room_name + "/" + target_file + '\n区块链hash:' + Hash)
    #user_to_proxy(json_data)
       #http://localhost/share/2020-02-24/19487307280%40chatroom/
       #http://39.99.224.190/2020-02-24/19487307280@chatroom/C:\Users\Public\nfs\data\langan\2020-02-24\19487307280@chatroom\1484ec68e1f4c18966e9a595583af1aa.jpg
    return reply_msg, get_room_wxid(msg_data)  
    
def process_text_msg_data(msg_data):
    if get_msg_sender(msg_data) == "管理员":
        return
    room_name = get_room_name(msg_data)
    task_id = get_user_task(room_name)
    value = "1"
    FileDir = DATA_DIR + "\\" + task_id + "\\" + room_name + "\\"
    mkdir(FileDir)
    target_file = save_text_file(FileDir, get_text_content(msg_data))
     ######################## blockchain ###############################
    json_data = {'taskid_userid': task_id + room_name, 'message': target_file}
    r = user_to_blockchain(json_data)
    Hash = json.loads(r.text).get('Hash')
    ###################################################################
    #json_data = {'action': "user_to_proxy", 'value': value, 'task_id': task_id, 'room_name': room_name, 'message': FileDir+msg['FileName'], 'Hash': Hash}
    reply_msg = ('您的信息已被记录 http://39.99.224.190/share/' + task_id + "/" + room_name + "/" + target_file + '\n区块链hash:' + Hash)
    #user_to_proxy(json_data)
       #http://localhost/share/2020-02-24/19487307280%40chatroom/
       #http://39.99.224.190/2020-02-24/19487307280@chatroom/C:\Users\Public\nfs\data\langan\2020-02-24\19487307280@chatroom\1484ec68e1f4c18966e9a595583af1aa.jpg
    return reply_msg, get_room_wxid(msg_data)  
    
#-------------------------------------------------------------------------------------------
@app.route('/recieve_msg', methods=['POST'])
def recieve_msg():
    res = []
    reply_msg = []
    wxid = []
    
    if request.method != 'POST':
        app.logger.info("recv data is:%s", str(request.get_data()))
        return jsonify(["暂时只支持Post方式"])

    request_object = json.dumps(request.json)
    print ("收到消息" + request_object)
    msg_data = get_msg_data(request.json)
    action = get_msg_action(msg_data)
    print ("action:" + action)
    
    if action == "reportContact":
        update_room_dict(msg_data["data"]["groupList"]) 
        
    elif action == "reportChatroomMessage":
        reply_msg, wxid = process_ChatroomMessage_msg_data(msg_data)
        
    elif action == "reportVideoMessage" :   
        reply_msg, wxid = process_video_msg_data(msg_data)
  
    elif action == "reportVoiceMessage":
        reply_msg, wxid = process_voice_msg_data(msg_data)
       
    elif action == "reportPicMessage":
        reply_msg, wxid = process_pic_msg_data(msg_data)
    
    elif action == "reportTextMessage":
        reply_msg, wxid = process_text_msg_data(msg_data)
        
    else:
        app.logger.info("recv data is:%s", str(request.get_data()))
        #return jsonify(["不支持的action类型"])
    
    if action == "reportVideoMessage" or action == "reportVoiceMessage" or action == "reportPicMessage" or action == "reportTextMessage":
        send_text_to_user(reply_msg, wxid) 
        writelog('./recieve.log', str(request_object))
        
    return jsonify(res)
    
#-------------------------------------------------------------------------------------------   
def send_text_to_user(reply_msg, wxid):
    print("send_text_to_user*************************************" + reply_msg + wxid)
    send_dict = {"api":"sendTextMessage", "sendId":"","option":{"wxid":wxid, "text": reply_msg}}
    wexin_cmd_queue.put(send_dict)
    
#-------------------------------------------------------------------------------------------
@app.route('/send_msg', methods=['GET'])
def send_msg():
    #cwxid  = request.args.get('wxid')
    #pid = request.args.get('pid')

    res = []
    init_getContact()   #初始化群信息，仅执行一次
    #res = send_dict
    
    while not wexin_cmd_queue.empty():
        send_dict = wexin_cmd_queue.get()
        #print ("get !!!!!!!!!!!!!!!!!!!!!!!!!"+ send_dict)
        res.append(send_dict)

    #res = []
    
    for i in res:
        print("发送给微信的命令开始：")
        print(i)
        print("发送给微信的命令结束")
    return jsonify(res)

#-------------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567, debug=False)
    