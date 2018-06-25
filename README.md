# IoT-Project
Iot課程Projet

1.首先先把記憶SD卡格式化避免裏頭有殘留檔案

2.下載Raspberry pi OS--https://www.raspberrypi.org/downloads/raspbian/ 可以至此下載。

3.依照他的導覽https://www.raspberrypi.org/documentation/installation/installing-images/README.md 安裝OS image。

4.安裝miniconda 於此網址依照步驟安裝 https://conda.io/miniconda.html。

5.https://conda.io/docs/user-guide/tasks/manage-environments.html 依網站內容創造虛擬環境，之後所有動作在虛擬環境中進行可以避免搞壞Raspberry Pi本身的內容，若是裝錯了、弄壞了，刪掉虛擬環境重新創一個虛擬環境重來即可。

6.可用內建Thonny進行程序編寫，不過我習慣用了nano。

7.nano 檔名.py 便可以撰寫python程式。

執行便是 python 檔名.py。
https://www.w3schools.com/nodejs/default.asp 依照此網址步驟可以安裝好Node.js以及相關基礎運作。
Node.js可以架設一伺服器在Chrome供Javascript運行然後再由手機開啟網頁進去Node.js創的伺服器去操作車車，但是因為時間關係 我沒做出來...
超音波感測器的部分因為電阻不對，我都接好線、Code也打完可是出不來估計是電流過小。

PS.Schematic圖中接GPIO的口依序由上至下改為接BCM 12、13、19、26

結果最後我只能用這個test2.py設定讓他前進後退及左右轉()中為秒數可以控制要運行幾秒。這個車的輪胎買來不太能動，我還特地去買兩張砂紙來磨他的輪胎，結果還是不是很好動。因為材料的晚到加上期末考的摧殘，我自己對於這個成果相當不滿意，想說還能做得更好更接近Proposal，所以我想說能不能留下這些材料留過一個暑假自己有時間再多做看看能不能離目標Project 的Proporsal近一點，無關乎分數，不過好像沒有辦法，必須歸還系辦，只能等以後有資金自己買來才能用了！感謝老師帶我找到進入IoT的大門，這樣講可能感覺有點矯情，不過這真的是我想說的，一開始燈泡會亮、能讓七節管亮、剛能讓車子動，每次有點東西出來都帶給我超大的感動，雖然只是一點點小皮毛，可是還是很感動，感覺自己好像終於弄出了點什麼。
不過後面雖然挫折更多一直做不出來，但是卻讓我更想做出來的心燃起來了。可惜時間和器材不允許，最後George，謝啦！

Demo影片
https://youtu.be/625UvIt-cRo

參考資料
http://www.piddlerintheroot.com/l298n-dual-h-bridge/
https://www.piddlerintheroot.com/project-nomad/
https://pimylifeup.com/raspberry-pi-distance-sensor/
http://www.codedata.com.tw/javascript/using-nodejs-to-learn-javascript-3-function-parameter-closure/
https://github.com/EnotionZ/GpiO/blob/master/test/tests.js
https://github.com/amphancm/RasberryPi_NodeJS_Control_LED
https://github.com/dapiddler/NOMAD/blob/master/nomad.py
https://www.w3schools.com/js/js_json.asp
https://www.w3schools.com/nodejs/nodejs_events.asp

