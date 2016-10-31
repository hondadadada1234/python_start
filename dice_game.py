# coding: utf-8
import dice

num = input('4,6,8,12,20のどれで勝負しますか？：') # input関数を使って値を受け取る

my_dice = dice.Dice(num)
cpu_dice = dice.Dice(num)

my_pip = my_dice.shoot()
cpu_pip = cpu_dice.shoot()

print('CPU：' + str(cpu_pip) + ' あなた：' + str(my_pip))

#状況によってメッセージかえる
if my_pip > cpu_pip:
  print('あなたの勝ち')
elif my_pip < cpu_pip:
  print('あなたの負け')
else:
  print('ひきわけ')
