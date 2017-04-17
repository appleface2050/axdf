##anxindianfu.com
### 


<h3 id="1">首页交流-获取数据</h3>
GET api/talk
<br>
<table>
   <tr>
	  <td>parameter</td>
	  <td>comment</td>
	  <td>required</td>
   </tr>
</table>


<h3 id="1">首页交流-提交数据</h3>
POST api/talk
<br>
<table>
   <tr>
	  <td>parameter</td>
	  <td>comment</td>
	  <td>required</td>
   </tr>
   <tr> <td>text</td>  <td>发消息人账号</td>  <td>Y</td></tr>
   <tr> <td>text</td>  <td>消息内容</td>  <td>Y</td></tr>
</table>

<h3 id="1">发手机验证码</h3>
GET api/send_sms_code
<br>
<table>
   <tr>
	  <td>parameter</td>
	  <td>comment</td>
	  <td>required</td>
   </tr>
   <tr> <td>tel</td>  <td>手机号</td>  <td>Y</td></tr>
</table>

-------------------