# MHRV-RS Hider : A Project to improve the security of using mhrv-rs

### How it works: 

There are several ways to improve the security of not just Mhrv-rs, but any VPN/Proxy, one of which is just knowing when to use them.
During Internet Blockouts Or any other time, the best time to use a Risky VPN/Proxy is at the peak of traffic usage, not at 3 a.m .
So This project forbids the user from using Mhrv-rs past 12 p.m. unless they explicitly state they want to.

Another way to improve security is to limit the amount of time the VPN is used, so this project forbids the user from using the VPN for more than 15 minutes unless 
they input another amount of time. 

The last and the most important thing is having a Chaffer, a Chaffer is basically something that keeps pinging / sending data to Not so risky sites so the user's 
VPN traffic is lost in them. 

### How to use :

Read the documentation and how to install in the Mhrv-rs Repo, and then just run 

`python3 mhrv-rs-hider.py`

If you want to use it past 12 p.m. ( Not recommended ) : 

`python3 mhrv-rs-hider.py past_12=true`

If you want to state for what amount of time you want to be using mhrv-rs ( in seconds ) :

`python3 mhrv-rs-hider.py time=1800` ( 30 minutes )

Full example :

`python3 mhrv-rs-hider.py time=1800 past_12=true`


