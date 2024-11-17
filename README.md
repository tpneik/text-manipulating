# This documentation is for text manipulation

Example we have data like this:
```text

DOS/Rate Limiting Policy:
42.96.51.166 (Vietnam) --> 10.16.1.50 (KDJB-PROXY) [1367]

DOS/Rate Limiting Policy:
42.96.51.166 (Vietnam) --> 10.16.1.50 (LFV-PROXY) [1596]


DOS/Rate Limiting Policy:
42.96.51.166 (Vietnam) --> 10.16.1.50 (CRY-PROXY) [2208]
42.96.51.166 (Vietnam) --> 10.16.1.101 (ONY-VIP) [411]

DOS/Rate Limiting Policy:
14.225.231.230 (Vietnam) --> 10.16.1.101 (TRD-VIKP) [1264]
14.225.231.239 (Vietnam) --> 10.16.1.101 (TDJ-VHIP) [26]

DOS/Rate Limiting Policy:
14.225.231.239 (Vietnam) --> 10.16.1.101 (LJK-POP) [44]
```
We want to take the data of source and destination of it.

---> Use regex with python

Take a look at the thing we want to get. It have the format as:

```
IP (Country) --> IP (Server)
```
We can turn it into regex as follows:

```
(\d{1,3}(.\d{1,3}){3}) \(\w+\) --> (\d{1,3}(.\d{1,3}){3})
```
You can alse use this [website](https://regexr.com/) as regex editor ! Hehe

```python

result = re.finditer(r"(\d{1,3}(.\d{1,3}){3}) \(\w+\) --> (\d{1,3}(.\d{1,3}){3})", data_string)
data = list({i.group(1) for i in result})
print(data)
```
Explain about this code (specificly in line2):
Function finditer will find all the substring as regex describe and put it into the iterators (just a kind of list hehe). 

The number inside group means the number pair of Parentheses "()"
Ex: 
```
(somwthing) (went) (wrong)
1 --> somwthing
2 --> went 
3 --> wrong

/// Much special

(something (went)) (wrong) (now)
1 --> something went
2 --> went
3 --> wrong
4 --> now
```
In the situation above, I use (1), means that only take the source IP.


Back to the line2 in python code, the thing inside the bracket:

```
i.group(1) for i in result
   ^
   
```
The thing before "for" can manipulate every single element in your array (list,..). You also can use the function can return the result to it.
The bracket with list allow you to choose unique value. Its call list comprehension!