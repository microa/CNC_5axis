## CNC_5axis (English Version)
<br>

<br>Packages needed:
<br>* pyserial
  <br>-> pip install pyserial
  <br>-> https://pypi.org/project/pyserial/

<br>Three functions explainations: 

<br>* Move_Certain_Distance("COM48", "x", 20) 
<br>&nbsp; UART port: COM48 
<br>&nbsp; Input "x","y", or "z" to control X-axis, Y-axis, or Z-axis respectively. 
<br>&nbsp; The number 20 represents relative distance from the origin.

<br>* Move_Certain_Time("COM48", "x", "forward", 2) 
<br>&nbsp; UART port: COM48 
<br>&nbsp; Input "x","y", or "z" to select X-axis, Y-axis, or Z-axis respectively. 
<br>&nbsp; Input 'forward' or 'backward' to choose the motor's direction. 
<br>&nbsp; The number 2 represents the duration to move for 2 seconds and then stop. 

<br>* Set_Move_Speed("COM48", "xyz") 
<br>&nbsp; UART port: COM48 
<br>&nbsp; Input "xyz" or "ab"  to adjust the speed of the corresponding axises or motors. 

<br>You can select "a" or "b" in addition to "x", "y", and "z".

<br>
<br>## CNC_5axis （中文版）

<br>需要安装的python包:
<br>* pyserial
  <br>-> pip install pyserial
  <br>-> https://pypi.org/project/pyserial/

<br>已开发三个主要功能： 

<br>* Move_Certain_Distance("COM48", "x", 20) 
<br>&nbsp; 串口号： COM48 
<br>&nbsp; 输入 "x","y", or "z" 以分别选中 X-轴, Y-轴, or Z-轴 
<br>&nbsp; "20"表示移动距离原点的相对距离

<br>* Move_Certain_Time("COM48", "x", "forward", 2) 
<br>&nbsp; 串口号： COM48 
<br>&nbsp; 输入 "x","y", or "z" 以分别选中 X-轴, Y-轴, or Z-轴 
<br>&nbsp; 输入 "forward" 或 "backward" 以选择电机的 正向 或 反向 运动 
<br>&nbsp; 数字 "2" 表示执行运动的时间，单位是秒 

<br>* Set_Move_Speed("COM48", "xyz") 
<br>&nbsp; 串口号： COM48 
<br>&nbsp; 输入 "xyz" 或 "ab" 以选中需要调节速度的对象（电机组）. 

<br>补充：除 "x", "y", 和 "z" 以外，上述函数中还可以选择 "a" or "b"
