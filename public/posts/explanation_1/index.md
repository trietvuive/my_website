# Dumb it down: Edmond-Karps, Max-Flow-Min-Cut, Support Vector Machine, VPC/Networking


Besides sleeping and watching anime, I also do some studying too (emphasized on **some**).
Sometimes, I read on topics from [Algorithm/Competitive Programming](https://cp-algorithms.com), continuing my [Coursera course on ML](https://www.coursera.org/learn/machine-learning)
, or continue to blow shit up in AWS just because. I also forget stuff pretty quickly, 
so I'll try to document what I learned today here. Also try to see how deep I really understand what I read because if you can't understand what 
I'm talking about here (even if you aren't a CS major), then there's a high chance I just don't know what I'm talking about. Here we go:

## Edmond-Karps 

Edmond-Karps is a max-flow algorithm. What's max-flow? Well, imagine you wanna pump water through a bunch of pipes to your neighbor's house to piss them off, 
but each pipes can carry a different max amount of water. But you wanna pump as much water as possible!

![s is where you start pumping, t is the destination](https://raw.githubusercontent.com/e-maxx-eng/e-maxx-eng/master/img/Flow1.png)

Note that you don't pay the water bill. How do you do it? (However, you will pay if the pipe bursts).

Edmond-Karps say you keep pumping. You find a path where all the pipes on that path can still carry water, and you keep pumping.
Note that you can only carry the minimum of what all pipes on that path can carry. Ex: If the pipes on your path can carry 2,3,5,7, then you can only make 
them all carry 2 (cuz you pay if the 2 pipe burst).

![Ah, that is enough water right?](https://raw.githubusercontent.com/e-maxx-eng/e-maxx-eng/master/img/Flow7.png)

So you pump, and you get to this. We're done!...?

![What?](https://raw.githubusercontent.com/e-maxx-eng/e-maxx-eng/master/img/Flow8.png)

What does that picture even mean? It means instead of D pumping 3 to A, D only pumps 2, and s will compensate for that missing 1. 
Instead, D will use the extra 1 to pump to C. Extra water!

![Now that will show your neighbor](https://raw.githubusercontent.com/e-maxx-eng/e-maxx-eng/master/img/Flow9.png)

How did you even find this? Well, same thing as last time, we will try to find path that we can still pump water through. 
However, we'll have a trick up our sleeve. When D pumps 3 to A, we will tell A that it can pumps 3 to D! Wait, what? But we can't go from A to D... You might say. Not with that attitude!

Think about this, and lmk if it makes sense. You have 3 going to D (from somewhere) and you pump that 3 to A. However, let's say A have too much water and wanna return 2 back to D. Instead of physically pumping from A to D, 
we'll just tell D to pump 3-2 = 1 to A instead of 3. It still results in the same situation: Instead of D pumping 3 to A and A pumping 2 back, D only pumps 1 to A. Although we can't do the former irl, we can ~~cheat~~ 
use that model to handle tricky situation where we need to return water back to use on another pipe that needs it more.

So that's that. Next time you need to flood your neighbor's house, remember to use [Edmonds-Karp algorithm](https://cp-algorithms.com/graph/edmonds_karp.html).

## Max-Flow-Min-Cut

Max-Flow-Min-Cut Theorem say that when you're done flooding your neighbor's lawn, you can keep the map of all the pipes and how much water they carry.

On that piece of paper, you'll can divide all the nodes (nodes are the circle thingy where your water is stored) into 2 groups: A group with the source node (where you start pumping) 
and a group with the destination node (your neighbor's house). Pick randomly. You'll find that, no matter how much you try, the amount of water that flow from the 
source group to the destination group won't be smaller than the max flow (i.e how much water you were able to pump to your neighbor's house).

![5 from A to B, 3 from A to C, and 2 from D to C = 10 total](https://raw.githubusercontent.com/e-maxx-eng/e-maxx-eng/master/img/Cut.png)

The reason: All water from your house eventually flow to your neighbor's house. That's your max flow. Therefore, water from your source node and any nodes you pick for source group will find its way to the neighbor's house, or through a node in the destination group before entering your neighbor's house.
That's where our minimum of 10 come from. And the min-cut-max-flow theorem said that the minimum amount of water from source group to destination group (i.e min-cut) = your max flow.

However, some nodes from the destination group (because you pick randomly) might pump water back to your source group temporarily. Because we only count water from source group to destination group, this means 
the source group get to reuse that water: they pump it to destination, destination return it temporarily, and they pump it back again to destination (remember all water ultimately ends in your neighbor's lawn). 
That's why some source/destination group configuration will have more water flowing from source to destination groups than max flow (btw, dividing all nodes to source/destination is called cut. You basically cut it into 2 groups).

I think I explained that like shit, but oh well. Feel free to read more. One last thing: You can find any min-cut by starting from source, go through any pipe that can still carry water and add those nodes to source group 
(including those opposite pipes we were talking about). 

Some caveat: 

_There's one simplest min-cut. It's the source node vs everyone else. 

_There are min-cut that you cannot discover by only going through pipe that can still carry water. Imagine a network where all pipes are maxed out.

_The reason why this works (I think, they didn't clarify this) is that any min-cut cannot have water from destination go back to source (because source can reuse that water, effectively increasing the amnt of water from source to dest). 

You eliminate this possibility by going through the opposite pipe that we talked about and add that node to your source group.  Theoretically, any cut where no destination node pump water to source node would qualify as min-cut.

Tired yet? Still have 2 more to go!

## Support Vector Machine

This section is only for those who know what I'm talking about. Feel free to skip it.

So in Machine Learning, there's this thing called Support Vector Machine (SVM). I won't even bother with how it works so feel free to look it up lmao.

SVM is also a large margin classifier, which means it will try to draw a decision boundary with large distance between classes. And this only really works when C, the parameter you multiply with the cost parameter, is high.

I was initially confused by this, even after looking through the vector stuff. Since C is high, I thought that the SVM can compensate by just making theta obscenely high, since regularization doesn't matter to it as much as the cost parameter.

However, after thinking it over, I realized that it could do that, but it can do better by just picking a large margin instead, since it's still punished quadratically for making theta high. 
In fact, large margin is implicitly encouraged by making C high. In contrast, when C is low, it can just underfit and make close decision boundary, since it cares more about making theta low. But yea, the large margin thing was quite interesting. Idk. 

## VPC

So I'm reading a book about AWS (cuz I'm a nerd) while also blowing shit up in the console. But I'm poor, so I try not to blow too much up. 

Anyway, I was reading about VPC and networking, and I'm not exactly any good at networking. I thought I'll just list some term here and try my best to define them. Feel free to check it if you actually know what they are; 
feel free to lmk if you understand (because if you don't, then I prob don't understand it that well):

VPC: Virtual Private Cloud. Basically networking stuff so that you manage all the connections and won't be featured on [haveibeenpwned.com](https://haveibeenpwned.com).

CIDR blocks: A huge continuous block of IP. AWS give your VPC a primary CIDR blocks to mess with.

IP(v4): I'm still not sure if I understand it well. Just know that it's used to connect you with stuff through Internet or your local network, or, in this case, VPC network. IPv4 is usually from 0.0.0.0 to 255.255.255.255.

Prefix length: Describes how many bits in the subnet, but more importantly, how many IP you have in the CIDR blocks. /24 means that the mask is xxx.xxx.xxx., therefore you can only go from xxx.xxx.xxx.0 to xxx.xxx.xxx.255. 
Also, lower is better, since you'll have less x, more range of IP address => more IP address. CIDR blocks are described with an IP mask and a prefix length. Ex: 192.168.0.0/16 means that you can go from 192.168.0.0 to 192.168.255.255, while 
192.168.0.0/24 means that you can only go from 192.168.0.0 to 192.168.0.255 (since 24 means you can't move around the first 3 of the 4 parts, kinda). Prefix length can go from 1 to 32 - it just means how many bytes the mask contains. But that will requires more explanation, 
so just remember it as how many IP the AWS overlord gives you.

IP(v6): No lul. It's still pretty cool and good tho.

Subnet: Within your CIDR blocks, you can chop those IP addresses up into subnet to use for different purpose. My book mentions that you can chop some for web server and some for database server, so that's that. Also, you cannot 
have subnets with overlapping range, and they must be all within the range of the VPC CIDR block.

Also, apparently AWS also took the first 3 IP address and the last one in every subnet for fun. You can't complain to Jeff Bezos for this one, altho you can complain to the new CEO, since he apparently used to lead AWS.

Also, that was wild. The dude who lead AWS is now the CEO of Amazon. I guess even they start to realize that AWS might be the new and better Amazon.com.

That's all for today. Fuck I need to actually sleep. I'll wake up tomorrow and see if I can actually understand what's being written here. I bet that 90% of this is incoherent anyway. 
I'mma go back to shitposting about anime tomorrow (not that this isn't shitposting, just a bit higher-quality than what I usually put on here).
