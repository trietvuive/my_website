---
title: "Big brain stuff I found on Codeforces"
date: 2021-07-08T22:27:44-04:00
draft: false

categories: [Programming]
tags: [CF]
---

There are a lot of big brain solutions on Codeforces. Or maybe I'm just too small-brained or haven't learned these things yet.

This was the problem I found today. 

![](/images/algorithms/codeforce.PNG)

As usual, I have no idea how to do this shit (within the time limit). I thought about DP, but then I saw the n <= 10^9. Any dp solution will probably requires at least N^2 - you'll
have to loop from 1 to 10^9, and then you have to find divisors of all number. There's no way it works within 2 seconds.

So I looked up the solution. One of the solution look like this (courtesy of Nxz)

~~~
#include <iostream>
using namespace std;
int main()
{
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        cout << ((n % 2 or (n == (n & -n)) && n % 3 == 2) ? "Bob\n" : "Alice\n");
    }

}
~~~

After thinking a bit, I think it works like this:

n == (n&-n) tests if n is a power of 2. You can try it yourself, but basically only binary representation that looks like 1000... will return true (2's complement of a power of 2 equals itself, basically).

n%3 == 2 tests if n is == 2 to the power of an odd number. 2^6 % 3 == 1, and 2^7 % 3 == 2.

Then, what this code basically saying is Bob wins if N is an odd number, or if N == 2^an odd number.
Let's see why this is the case.

First, you don't want N to be an odd number if it's your turn (because all primes are odd). When N is an odd number, there are 2 cases:

1. It's a prime. You're dead, because you can't pick any divisor. You lost.

2. It has an odd divisor. Note that no odd number has an even divisor. You pick the odd divisor, and your opponent get an even N (odd - odd == even)

The N that your opponent gets will have an odd divisor. Why? Because you subtract a divisor of N from N, so N can still be divided by that same divisor (if it's not, then the N you get was a prime, so you already lost).
Note that you cannot subtract N from N.

Therefore, this creates a cycle where you keep getting an odd number, forced to turn it into an even number, and your opponent then gives you back an odd number. Therefore, whoever gets the odd number lose, and since 
both players play optimally, they will avoid odd number at all cost. Therefore, if n is odd and you're first to act, you already lost.

However, that doesn't mean that if you're first to act and you get an even number that you automatically win. You only win if you gives the opponent an odd number. The exception to this is power of 2 number.

With power of 2, all of your divisors are even. You have 2 choices:

1. Choose a random even divisor and subtract it from N. The resulting even N will have an odd divisor, since any even number that's not a power of 2 has an odd divisor. Then, your opponent will choose that odd divisor, 
subtracting the odd divisor from the even resulting N, and you'll get an odd N. You lost.

2. Choose N/2. This is the only way to give your opponent an even N that's also a power of 2 so that they can't return you an odd number. Remember, all odd lose.

Since both players play optimally, they will choose 2 every time. Therefore, 4 = 2^2, 16 = 2^4, 64 = 2^6 will means the first player win (they will choose n/2 every time, and the second player will encounter 2 first and lose). 
8 = 2^3, 32 = 2^5, 128 = 2^7 will means the first player lose, since they will encounter 2 first when both players keep picking N/2. 

Feel free to play this out with a friend and check the result (assume you have friends). Game theory problems always intrigue me because there are interesting property, and you can actually play this with friends. 
Admittedly, they will just think you're a nerd, but some friends might think it's cool (plus, after all this, you should be able to beat them, since they probably won't play it optimally).

Anyway, about Anime. I jumped around between anime and haven't finished any yet. Not that I'm quickly bored, just that some animes are too good to finish. When you finished it, you just feel dead inside, and I'd rather not feel that. 
I think it's better for my mental health if I kept those good animes around for dark days so that I have something good to watch as a way to de-stress.