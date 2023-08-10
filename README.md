## CNC_5axis
<br>

Three functions explainations: <br>
<br>

* Move_Certain_Distance("COM48", "x", 20) <br>
&nbsp; UART port: COM48 <br>
&nbsp; Input "x","y", or "z" to control X-axis, Y-axis, or Z-axis respectively. <br>
&nbsp; The number 20 represents relative distance from the origin. <br>

* Moving("COM48", "x", "forward", 2) <br>
&nbsp; UART port: COM48 <br>
&nbsp; Input "x","y", or "z" to control X-axis, Y-axis, or Z-axis respectively. <br>
&nbsp; Input "forward" or "backward" to move the motor in the specified direction. <br>
&nbsp; The number 2 represents the duration to move for 2 seconds and then stop. <br>


* Speed("COM48", "xyz") <br>
&nbsp; UART port: COM48 <br>
&nbsp; Input "xyz" or "ab"  to adjust the speed of the corresponding axises or motors. <br>
