from app import db,User,Question
final=[{'question': 'HTML stands for :', 'option_1': 'Hypertext Messaging Language', 'option_2': 'Hypertext Mailing Language', 'option_3': 'Hypertext Markup Language', 'option_4': 'Hypertext Measuring Language', 'answer': 3},
       {'question': 'XML stands for :', 'option_1': 'Extra Markup Language', 'option_2': 'Extensible Markup Language', 'option_3': 'Example Markup Language', 'option_4': 'Expert Markup Language', 'answer': 2},
       {'question': 'PaaS stands for :', 'option_1': 'Password as a Service', 'option_2': 'Python as a Service', 'option_3': 'Plugin as a Service', 'option_4': 'Platform as a Service', 'answer': 4},
       {'question': 'SaaS stands for :', 'option_1': 'Security as a Service', 'option_2': 'Software as a Service', 'option_3': 'Server as a Service', 'option_4': 'Service as a Service', 'answer': 2},
       {'question': 'GCP stands for :', 'option_1': 'Google Consultancy Product', 'option_2': 'Google Consultancy Platform', 'option_3': 'Google Cloud Platform', 'option_4': 'Google Community Platform', 'answer': 3},
       {'question': 'IaaS stands for :', 'option_1': 'Infrastructure as a Service', 'option_2': 'Internet as a Service', 'option_3': 'IOT as a Service', 'option_4': 'Identity as a Service', 'answer': 1},
       {'question': 'AWS stands for :', 'option_1': 'Amazon Wide Services', 'option_2': 'Amazon Withdraw Services', 'option_3': 'Amazon Writing Services', 'option_4': 'Amazon Web Services', 'answer': 4},
       {'question': 'HTTP stands for :', 'option_1': 'Hypertext Transfer Protocol', 'option_2': 'Hypertext Transition Protocol', 'option_3': 'Hypertext Transportation Protocol', 'option_4': 'Hypertext Triggering Protocol', 'answer': 1},
       {'question': 'VPC stands for :', 'option_1': 'Variable Path Controller', 'option_2': 'Variable Path Creater', 'option_3': 'Virtual Private Cloud', 'option_4': 'Virtual Private Controller', 'answer': 3},
       {'question': 'VPN stands for :', 'option_1': 'Variable Path Network', 'option_2': 'Virtual Path Network', 'option_3': 'Virtual Planning Network', 'option_4': 'Virtual Private Network', 'answer': 4}]
for q in final:
    temp=Question()
    temp.question=q["question"]
    temp.option_1=q["option_1"]
    temp.option_2=q["option_2"]
    temp.option_3=q["option_3"]
    temp.option_4 =q["option_4"]
    temp.answer = q["answer"]
    db.session.add(temp)
    db.session.commit()
