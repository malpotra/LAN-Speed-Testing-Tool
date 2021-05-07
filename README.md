# LAN-Speed-Testing-Tool
1. The script displays the time taken for a round trip from sender to receiver.
   ![Sample Run](https://user-images.githubusercontent.com/56645001/117440267-72e8c000-af51-11eb-8fe0-f3cbfb899b48.png)
 
3. It works for at least 2 devices on a LAN. 
![Case when there is only 1 device on the LAN](https://user-images.githubusercontent.com/56645001/117440531-cce98580-af51-11eb-9d5b-3ba6fd7170d1.png)


5. The user just has to run the script(main.py), a broadcast request finds out the first available device on the LAN other than the user's device. 
6. The results are represented in a fashion similar to what can be seen on the windows command prompt. 

#### How it is different from the in built ping command in Windows Command Prompt?
For this code there is no need to know the IP address of the receiver prior to sending the ping request, the script is written in such a manner that it finds itself the IP address of a device on the network, the user just has to run it and forget about everything else. For the inbuilt ping command the correct IP address of the receiver must be known in advance in order to get the correct results.
