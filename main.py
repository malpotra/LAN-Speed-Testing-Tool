from scapy.all import*
from time import*

#Works for only 2 devices on a LAN (if more than one are present it will consider the first device)
#The User Just has to run the script. No need for giving the ip from stdin

my_router_ip=conf.route.route("0.0.0.0")[2]
print("My router ip is  "+my_router_ip)
my_ip=get_if_addr(conf.iface)
print("My ip is "+ my_ip)
print("\n")

#broadcast to know all the devices on the LAN 
target_ip=my_router_ip+"/24"
arp=ARP(pdst=target_ip)
ether=Ether(dst="ff:ff:ff:ff:ff:ff")
packet=ether/arp
other_computer_ip=None
print("Getting the devices on the LAN...")
while other_computer_ip == None:
    result=srp(packet,timeout=3,verbose=0)[0]
    for sent,received in result:
        if received.psrc != my_router_ip and received.psrc != my_ip:
            other_computer_ip=received.psrc
#the target ip is the object other_computer_ip
print ("\nAvialable devices in the network:")
print ("IP")
print (my_ip+"\tMy device ")
print (other_computer_ip+"\tThe other device\n")

a=IP()
a.dst=other_computer_ip
#packet to be sent
packet2=a/ICMP()/"Hello Friend"
pkt_size=len(packet2)
print("Pinging "+other_computer_ip+" with ", pkt_size, end=" ")
print("bytes of data:")

time_sum=0
received=0
lost=0
for x in range (4):
    t1=time()
    response=sr1(packet2,timeout=3,verbose=0)[0]
    t2=time()
    time_taken=t2-t1
    if response == None:
        print("Request timed out")
        lost=lost+1
    else:
        print ("\tReply from "+other_computer_ip+": bytes=",pkt_size,end=" ")
        print ("time=",int(time_taken*1000),end=" ms")
        print (" TTL=",response.ttl)
        time_sum=time_sum+time_taken
        received=received+1

percent_loss=int(lost*100/4)
average_time=time_sum/received

print("\nPing stats for "+other_computer_ip+":\n\tPackets: Sent = 4, Received = ",received,", Lost = ",lost," (",percent_loss,"% loss)")
print("Approximate round trip times in milli-seconds:\n\tAverage = ",int(average_time*1000),"ms")
