# Evaluating OCR output

A little Python script that parses a bunch of text files, seperates the words and checks with Hunspell whether the word checks out or not.  
It reports the total number of words, the number of bad ones, and the percentage.

I needed this for a project where we use _ScanTailor Advanced_ to pre-process scans of typewriter pages before _Tesseract_ tries to make sense of it. Fiddling with the threshold value in ST produces visible differences in OCR output: Some words will be correct with a low threshold and fall apart when you raise the threshold. Other words behave vice versa.

The script tries to quantify this in a crude manner, so I could make an informed decision about the threshold value. The differences found are minimal, but it shows a clear pattern: more threshold produces better results. This is higly dependent on you content.

Uses [spylls](https://github.com/zverok/spylls) and Hunspell. Expects a german dictionary in `/usr/share/hunspell/de_DE`, as it is the case in Ubuntu.

Usage:
~~~
$ ./spellcount.py <target folder>
~~~

---

### Findings

2022-12-10  
Processing VNS-005 / 08

| Threshold in ScanTailor | Words | Errors | Ratio   |
| ----------------------- | -----:| ------:| -------:|
| -100                    | 3578  | 424    | 11.85 % |
| -50                     | 3580  | 392    | 10.95 % |
| 0                       | 3579  | 381    | 10.65 % |
| 50                      | 3580  | 356    | 9.94 %  |
| 100                     | 3577  | 341    | 9.53 %  |


~~~
0
Found 7 textfiles.
Reporting 3579 words and 381 spelling errors.
The error ratio is 10.65 percent.

100
Found 7 textfiles.
Reporting 3577 words and 341 spelling errors.
The error ratio is 9.53 percent.

-100
Found 7 textfiles.
Reporting 3578 words and 424 spelling errors.
The error ratio is 11.85 percent.

-50
Found 7 textfiles.
Reporting 3580 words and 392 spelling errors.
The error ratio is 10.95 percent.

50
Found 7 textfiles.
Reporting 3580 words and 356 spelling errors.
The error ratio is 9.94 percent.
~~~