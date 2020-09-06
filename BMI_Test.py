import time
r=1
print("欢迎使用体重指数(BMI)测试！\n开发者：Jacob_Hu\n本程序Github库地址:https://github.com/JacobHu0723/BMI_Test\n如有Bug请在Github下Issues进行反馈！")
print("")
time.sleep(1)
print("体重指数(BMI)计算公式：BMI=体重(kg)/身高(m)^2\n\n按照《信息技术 必修一》P63实践活动标准\n性别\t等级\t体重指数/(kg·m^-2)\n男生\t正常\t16.5~23.2\n男生\t低体重\t≤16.4\n男生\t超重\t23.3~26.3\n男生\t肥胖\t≥26.4\n女生\t正常\t16.5~22.7\n女生\t低体重\t≤16.4\n女生\t超重\t22.8~25.2\n女生\t肥胖\t≥25.3\n")
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
        print("你的体重","\033[4;32m正常\033[0m")
      elif bmi<=16.4:
        print("你的体重","\033[4;34m过轻\033[0m")
      elif bmi>=23.3 and bmi<=26.3:
        print("你的体重","\033[4;33m超重\033[0m")
      elif bmi>=26.4:
        print("你的体重""\033[4;31m肥胖\033[0m")
    elif s==2:
      if bmi>=16.5 and bmi<=22.7:
        print("你的体重","\033[4;32m正常\033[0m")
      elif bmi<=16.4:
        print("你的体重","\033[4;34m过轻\033[0m")
      elif bmi>=22.8 and bmi<=25.2:
        print("你的体重","\033[4;33m超重\033[0m")
      elif bmi>=25.3:
        print("你的体重","\033[4;31m肥胖\033[0m")
    elif s!=1 and s!=2:
      print("性别输入错误")
    time.sleep(0.5)
    r=int(input("是否再测一次？（输入1再测一次，输入2结束测试）"))
time.sleep(0.5)
print("感谢你的使用！")
