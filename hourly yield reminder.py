import traceback
import requests

# 飞书机器人 Webhook 地址，需要替换为你自己的地址
webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/×××××××××××××××'


# 发送飞书消息的函数
def send_message(message, webhook_url):
    data = {
        "msg_type": "text",
        "content": {
            "text": message
        }
    }
    response = requests.post(webhook_url, json=data)
    return response


try:
    # 需要监听的代码
    import json
    import requests
    import mysql
    import mysql_total
    import mysql_today
    import mysql_act
    import mysql_compare
    import mysql_schedule  
    import token_post


    def send():
        url = "https://open.feishu.cn/open-apis/im/v1/messages"
        params = {"receive_id_type": "chat_id"}

        card = json.dumps({
            "elements": [
                {
                    "tag": "markdown",
                    "content": "**当前班次：{shift}**\n**班次时间：{starttime}~{endtime}**"
                },
                {
                    "tag": "div",
                    "fields": [
                        {
                            "is_short": True,
                            "text": {
                                "tag": "lark_md",
                                "content":"**上线计划：**{today_plan1}\n**今日上线：**{today_act1}\n**总完成率：**{todat_percent1}\n**班次计划：**{plan1}\n**班次上线：**{a1}\n**班次完成率：**{percent1}\n"
                            }
                        },
                        {
                            "is_short": True,
                            "text": {
                                "tag": "lark_md",
                                "content": "**下线计划：**{today_plan2}\n**今日下线：**{today_act2}\n**总完成率：**{todat_percent2}\n**班次计划：**{plan2}\n**班次下线：**{a2}\n**班次完成率：**{percent2}"
                            }
                        }
                    ]
                },
                {
                    "tag": "div",
                    "fields": [
                        {
                            "is_short": True,
                            "text": {
                                "tag": "lark_md",
                                "content": "**班组小时产量：**\n**前处理&电泳**：{i}\n**钣金**：{j}\n**底涂**：{k}\n**密封**：{l}\n**电泳打磨**：{"
                                           "m}\n**面漆喷房**：{n}\n**检查精修**：{p}\n**报交**：{q}\n**注蜡**：{w}"
                            }
                        },
                        {
                            "is_short": True,
                            "text": {
                                "tag": "lark_md",
                                "content": "**实际/计划→差异**\n {pted}→{pted-}\n {check}→{check-}\n {mask}→{mask-}\n {"
                                           "sealing}→{sealing-}\n {sanding}→{sanding-}\n {tc}→{tc-}\n {polish}→{"
                                           "polish-}\n {finish}→{finish-}\n {wax}→{wax-}"
                            }
                        }
                    ]
                },
	{
      	"tag": "action",
      	"actions": [
        	{
          	"tag": "button",
          	"text": {
            	"tag": "plain_text",
            	"content": "当日产量统计(PC)"
          	},
          	"url": "http://10.232.65.1:8088/data/perspective/client/Li_Auto_Andon_CZ02/production",
          	"type": "primary"
        	}
      	]
    	}
            ],
            "header": {
                "template": "green",
                "title": {
                    "content": "班组产量小时推送",
                    "tag": "plain_text"
                }
            }
        })
        card = card.replace("{starttime}", str(mysql_schedule.shift_start_time))
        card = card.replace("{endtime}", str(mysql_schedule.shift_end_time))
        card = card.replace("{shift}", str(mysql_schedule.shift_result))
        card = card.replace("{i}", str(mysql.i[0]))
        card = card.replace("{j}", str(mysql.j[0]))
        card = card.replace("{k}", str(mysql.k[0]))
        card = card.replace("{l}", str(mysql.l[0]))
        card = card.replace("{m}", str(mysql.m[0]))
        card = card.replace("{n}", str(mysql.n[0]))
        card = card.replace("{p}", str(mysql.p[0]))
        card = card.replace("{q}", str(mysql.q[0]))
        card = card.replace("{w}", str(mysql.w[0]))
        card = card.replace("{plan1}", str(mysql_total.total[0]))
        card = card.replace("{plan2}", str(mysql_total.total[1]))
        card = card.replace("{a1}", str(mysql_act.act1[0]))
        card = card.replace("{a2}", str(mysql_act.act2[0]))
        card = card.replace("{today_plan1}", str(mysql_today.today_plan1[0]))
        card = card.replace("{today_plan2}", str(mysql_today.today_plan2[0]))
        card = card.replace("{today_act1}", str(mysql_today.today_act1[0]))
        card = card.replace("{today_act2}", str(mysql_today.today_act2[0]))
        card = card.replace("{todat_percent1}", str("{:.0%}".format(mysql_today.today_act1[0] / mysql_today.today_plan1[0])))
        card = card.replace("{todat_percent2}", str("{:.0%}".format(mysql_today.today_act2[0] / mysql_today.today_plan2[0])))
        card = card.replace("{percent1}", str("{:.0%}".format(mysql_act.act1[0] / mysql_total.total[0])))
        card = card.replace("{percent2}", str("{:.0%}".format(mysql_act.act2[0] / mysql_total.total[1])))
        card = card.replace("{percent1}", str("{:.0%}".format(mysql_act.act1[0] / mysql_total.total[0])))
        card = card.replace("{percent2}", str("{:.0%}".format(mysql_act.act2[0] / mysql_total.total[1])))
        card = card.replace("{pted}",
                            str(round(mysql_compare.pted_act[0])) + '/' + str(round(mysql_compare.finish_plan[0])))
        card = card.replace("{check}",
                            str(round(mysql_compare.check_act[0])) + '/' + str(round(mysql_compare.finish_plan[0])))
        card = card.replace("{mask}",
                            str(round(mysql_compare.mask_act[0])) + '/' + str(round(mysql_compare.finish_plan[0])))
        card = card.replace("{sealing}",
                            str(round(mysql_compare.sealing_act[0])) + '/' + str(round(mysql_compare.finish_plan[0])))
        card = card.replace("{sanding}",
                            str(round(mysql_compare.sanding_act[0])) + '/' + str(round(mysql_compare.finish_plan[0])))
        card = card.replace("{tc}", str(round(mysql_compare.tc_act[0])) + '/' + str(round(mysql_compare.finish_plan[0])))
        card = card.replace("{polish}",
                            str(round(mysql_compare.polish_act[0])) + '/' + str(round(mysql_compare.finish_plan[0]))
                            )
        card = card.replace("{finish}",
                            str(round(mysql_compare.finish_act[0])) + '/' + str(round(mysql_compare.finish_plan[0])))
        card = card.replace("{wax}",
                            str(round(mysql_compare.wax_act[0])) + '/' + str(round(mysql_compare.finish_plan[0])))
        pted = round(mysql_compare.pted_act[0] - round(mysql_compare.finish_plan[0]))
        if pted > 0:
            pted_dif = '+' + str(pted)
        else:
            pted_dif = str(pted)
        card = card.replace("{pted-}", pted_dif
                            )
        check = round(mysql_compare.check_act[0] - round(mysql_compare.finish_plan[0]))
        if check > 0:
            check_dif = '+' + str(check)
        else:
            check_dif = str(check)
        card = card.replace("{check-}", check_dif)
        mask = round(mysql_compare.mask_act[0] - round(mysql_compare.finish_plan[0]))
        if mask > 0:
            mask_dif = '+' + str(mask)
        else:
            mask_dif = str(mask)
        card = card.replace("{mask-}", mask_dif)
        sealing = round(mysql_compare.sealing_act[0] - round(mysql_compare.finish_plan[0]))
        if sealing > 0:
            sealing_dif = '+' + str(sealing)
        else:
            sealing_dif = str(sealing)
        card = card.replace("{sealing-}", sealing_dif)
        sanding = round(mysql_compare.sanding_act[0] - round(mysql_compare.finish_plan[0]))
        if sanding > 0:
            sanding_dif = '+' + str(sanding)
        else:
            sanding_dif = str(sanding)
        card = card.replace("{sanding-}", sanding_dif)
        tc = round(mysql_compare.tc_act[0] - round(mysql_compare.finish_plan[0]))
        if tc > 0:
            tc_dif = '+' + str(tc)
        else:
            tc_dif = str(tc)
        card = card.replace("{tc-}", tc_dif)
        polish = round(mysql_compare.polish_act[0] - round(mysql_compare.finish_plan[0]))
        if polish > 0:
            polish_dif = '+' + str(polish)
        else:
            polish_dif = str(polish)
        card = card.replace("{polish-}", polish_dif
                            )
        finish = round(mysql_compare.finish_act[0] - round(mysql_compare.finish_plan[0]))
        if finish > 0:
            finish_dif = '+' + str(finish)
        else:
            finish_dif = str(finish)
        card = card.replace("{finish-}", finish_dif)
        wax = round(mysql_compare.wax_act[0] - round(mysql_compare.finish_plan[0]))
        if wax > 0:
            wax_dif = '+' + str(wax)
        else:
            wax_dif = str(wax)
        card = card.replace("{wax-}", wax_dif)
        msgContent = json.loads(card)
        req = {
            "receive_id": "×××××××××××××××",  # chat id
            "msg_type": "interactive",
            "content": json.dumps(msgContent)
        }
        payload = json.dumps(req)
        headers = {
            'Authorization': token_post.strlist,  # your access token
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, params=params, headers=headers, data=payload)
        print(response.content)  # Print Response


    send()





except Exception as e:
    # 发送异常信息到飞书
    message = f"Error occured:\n{traceback.format_exc()}"
    send_message(message, webhook_url)
