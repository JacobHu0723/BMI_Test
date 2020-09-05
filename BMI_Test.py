import time
r=1
print("欢迎使用体重指数(BMI)测试！\n开发者：Jacob_Hu\n本程序Github库地址:https://github.com/JacobHu0723/BMI_Test\n如有Bug请在Github中进行反馈！")
time.sleep(1)
while r==1:
    s=int(input("请输入你的性别（男性请输1，女性请输2）:"))
    time.sleep(0.5)
    h=float(input("请输入你的身高（单位：m）"))
    time.sleep(0.5)
    w=float(input("请输入你的体重（单位：kg）"))
    time.sleep(0.5)
    bmi=w/(h**2)
    print("你的体重指数(BMI)为：",round(bmi,1))
    if s==1:
      if bmi>=16.5 and bmi<=23.2:
        print("你的体重为正常")
      elif bmi<=16.4:
        print("你的体重过轻")
      elif bmi>=23.3 and bmi<=26.3:
        print("你的体重超重")
      elif bmi>=26.4:
        print("你的体重肥胖")
    elif s==2:
      if bmi>=16.5 and bmi<=22.7:
        print("你的体重正常")
      elif bmi<=16.4:
        print("你的体重过轻")
      elif bmi>=22.8 and bmi<=25.2:
        print("你的体重超重")
      elif bmi>=25.3:
        print("你的体重肥胖")
    elif s!=1 and s!=2:
      print("性别输入错误")
    time.sleep(0.5)
    r=int(input("是否再测一次？（输入1再测一次，输入2结束测试）"))
time.sleep(0.5)
print("感谢你的使用！")
