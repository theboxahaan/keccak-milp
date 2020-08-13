# Keccak-MILP
## What This is All About
This repository contains the code for creating the MILP model to count the number of active SBoxes in each round of *Keccak-p* with block size of `400 bits`. The constraints are created by mostly following the method proposed by Mouha et. al. and its S-bP extension proposed by Sun et. al.

The "experiment" are the additional constraints on the `XOR` operation which help increase the accuracy of the predictions but seem to come at a cost. More on this later...

<img src="https://paper-attachments.dropbox.com/s_48455D6ADC8DFBB72F715F59DE88DEC845623C60D1CA368FED24D2707582F853_1589313553671_Screenshot+2020-05-13+at+1.29.00+AM.png" width="500px">

`mew.py` spits out a `.lp` file, which I fed into the Gurobi Optimizer to get the values of the optimized objective.
`keccak.py` is my implementation of Keccak which is in no way optimized for anything. I basically used it to check the validity of the results I was getting.
The table below shows the results visualised for 1 Round of *Keccak-p*[400]
<table>
  <tr>
    <th>x values</th>
    <th>y values</th>
    <th>z values</th>
  </tr>
  <tr>
    <td><img src="https://paper-attachments.dropbox.com/s_48455D6ADC8DFBB72F715F59DE88DEC845623C60D1CA368FED24D2707582F853_1589326471686_xval.png">
    </td>
    <td><img src="https://paper-attachments.dropbox.com/s_48455D6ADC8DFBB72F715F59DE88DEC845623C60D1CA368FED24D2707582F853_1589326436641_yval.png">
    </td>
    <td><img src="https://paper-attachments.dropbox.com/s_48455D6ADC8DFBB72F715F59DE88DEC845623C60D1CA368FED24D2707582F853_1589326498523_zval.png">
    </td>
 </tr>  
</table>

### Generating the `.lp` File
```bash
python mew.py --r [no. of rounds] > rounds.lp
```
This will output a file in the `LP Format` which can be used as input to a suitable solver. I used Gurobi.

<img src="https://www.gurobi.com/wp-content/uploads/2018/12/logo-final.png" width="150px">


## Observations
> I can see why this is not of much consequence :P

----
### References
1. [https://keccak.team/](https://keccak.team/)
2. [https://link.springer.com/chapter/10.1007/978-3-642-34704-7_5](https://link.springer.com/chapter/10.1007/978-3-642-34704-7_5)
3. [https://link.springer.com/chapter/10.1007/978-3-662-45611-8_9](https://link.springer.com/chapter/10.1007/978-3-662-45611-8_9)
