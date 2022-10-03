# Some fun technique I found while doing competitive programming puzzles: Regex DP


I do some competitive programming problems for fun, because I have a twisted sense of humor. Recently, I repeatedly encounter a pattern in those problems with a very elegant dynamic programming solution. </br>
I haven't seen anything like this elsewhere, although I'm somewhat aware that regex do use DP. The pattern I'm noticing is more of regex + subsequence. Let's give a concrete example:

> Given a sequence of 0 and 1. Supposed that you can choose any [l,r] interval and reverse them (only once). </br>
>
> What's the longest non-decreasing subsequence you can get? 
>
> Example input: [0,1,0,1] => 4. You can reverse [2,3] to get [0,0,1,1] and get 4. 
>
> Example input: [0,0,1,1,1,0,0,1,1,0] => 9. You can reverse [3,7] to get [0,0,0,0,1,1,1,1,1,0] and get 9.
>
> Note that this is a subsequence problem, not substring. If you have something like [0,1,0,1,0,1], you can still get 4 from picking [0,0,0,1].

Some initial approach I can think of is to count number of 0 as you go left and number of 1 as you go right. However, there's a more elegant solution. </br>

# Rephrasing the problem
Let's divide the sequence into 4 areas: A,B,C,D. A is left of B, B is left of C,... </br>
![Straight from Paint](/images/dp.png)

A and C is where you only pick 0, B and D is where you only pick 1. </br>

Our problem now becomes how to divide the subsequence into ABCD such that maximize the number of 0 you pick from A&C + number of 1 you pick from B&D. Note that A,B,C,D can be empty area. </br>

Why can the problem be formulated this way? Note that since you pick 0 from A&C and 1 from B&D, if you reverse B and C, you will have A C B D, with 0 coming from A and C and 1 coming from B and D. Then, the subsequence you pick will be non-decreasing.

The length of the subsequence above, if you choose ABCD that way, will be 2 + 3 + 1 + 3 = 9. For reference, the input sequence would be 0110 01110 110111 00111. 

Also, I'm aware that it's not neatly 4 bits. Deal with it =).

# Elegant dp solution

So now we rephrase the problem. But rephrasing the problem doesn't help if there's no elegant solution coming from it.
In comes dp.

```python
dp = [0] * 4
for c in s:
	for i in range(4):
		dp[i] = max(dp[i-1], dp[i] + (c % 2 == i % 2))
print(dp[3])
```

"What the hell did you just write?" You might ask.

Let's start with the array dp.

Here, dp[0] will be the max length if we only get to use A (aka only get to pick 0).

dp[1] will be the max length if we only get to use A and B (only pick 0 and pick 1 after 0). You don't have to use B, and if you don't, then dp[0] = dp[1].

dp[2] will be max length for A B C

and dp[3] will be max length for A B C D. 

We'll loop through the sequence. For every number, dp[1] will compare itself with dp[0]. If dp[0] is larger, that means the whole thing should've been in A.

Example: 00100. dp[0] will pick 00, skip 1, then pick 00. dp[1] will initially go with 001, skip 0, then realize that it would have been better off lumping the whole thing in A to get 4, because 4 > 3.

Then, dp[2] will constantly update with dp[1], dp[3] will constantly update with dp[2].

Note that putting 00100 in A will always be optimal. You can always switch to B anytime you like, but once you're in B you cannot switch back to A.

If you encounter a 0, you can +1 to dp[0] and dp[2], and if you encounter a 1, you can +1 to dp[1] and dp[3] (Hence the c % 2 == i % 2). Note that dp[1] might end up increase by 1 even if you encounter a 0 since it might decide it's better off to not start B yet and just lump the whole thing in A for the time being (aka the 00100 example).

I'm not too good at explanation, so if you are still with me at this point, then congrats! Then, the answer would be in dp[3], because dp[3] is where you get to use all of ABCD. Note that dp[3] would also be the largest number in dp, and dp[3] >= dp[2] >= dp[1] >= dp[0].

# Conclusion

The 4-liner python looks simple, but whoever invent this must have been a massive brain. This somewhat resembles constraints in algorithm where you would intentionally add more constraints to make the problem easier, then solve it and use the solution to solve the original problem.

In fact, that's the nature of dynamic programming: splitting problems into subproblems and use subproblems' solution for larger problem. However, I haven't seen this technique ever elsewhere outside of competitive programming (and even competitive programming book seems to not have it?)

That's why I named it regex dp. What it basically does is count the largest subsequence of a certain format (let's say you want the longest subsequence that follows 1234 - 1122344 for example. Then you would count longest 1, then longest 12, then longest 123, then longest 1234. If 1233 doesn't follow the rule, then your formula will look like max(dp[i], dp[i-1] + 1) instead). It bears a lot of similarity to problems like longest subsequence, but also doesn't really. The ABCD technique is also pretty neat, and whoever came up with this (probably someone in CP community, since I haven't encounter this outside of CP) must be pretty big-brained. Not me lol, though I do wish 😔.

PS: I watched a video on Hamming code by [3Blue1Brown](https://www.youtube.com/watch?v=X8jsijhllIA). Hamming code is also pretty elegant, and it must've take ton of trial and error to come up with such simple and elegant solution. Regex DP is also very elegant (though not that simple), and I can't imagine the amount of creativity that it takes to come up with this.
