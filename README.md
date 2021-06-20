# Keccak-MILP
## What This is All About
This repository contains the code for creating the MILP model to count the number of active SBoxes in each round of *Keccak-p* with block size of `400 bits`. The constraints are created by mostly following the method proposed by Mouha et. al. and its S-bP extension proposed by Sun et. al.

The "experiment" are the additional constraints on the `XOR` operation which help increase the accuracy of the predictions but seem to come at a cost. More on this later...


<img src="https://user-images.githubusercontent.com/32961084/122242358-e1ba2100-cee0-11eb-89e3-691e9468e6a7.png" width="80%">

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

### Solving the Model using Gurobi
```bash
$ gurobi_cl ResultFile='<resultfile.sol>' <modelfile.lp>
```


<img src="https://www.gurobi.com/wp-content/uploads/2018/12/logo-final.png" width="150px">


## Observations
> I can see why this is not of much consequence :P

## Results Table
| `r`   | `Best Objective` | `milp_model_1`     | `milp_model_2` |
|-------|------------------|--------------------|----------------|
| `1`   | `1`              | **`8.33s`      `(c)`** | **`7.21s   (c)`**  |
| `2`   | `4`              | `250.4s`    `(in)` | **`137.94s (c)`**  |
| `3`   | `10`             | `1121.38s`  `(in)` |                |
| `4`   | `102`            | `940s`      `(in)` |                |

<sub><b><i>completed(c), incomplete(in)</i></b></sub>
<sub>▲ The incomplete(in) times are Gurobi run-times</sub>

> For `model_1` apart from the `r=1` run, all other runs were interrupted runs.
> Looking for some serious computing power 🚀 

## Update
Results from `milp_model_2_gen.py` are wayyy faster than `milp_model_1_gen.py` as some constraints have been optimized.

----
### References
1. [https://keccak.team/](https://keccak.team/)
2. [https://link.springer.com/chapter/10.1007/978-3-642-34704-7_5](https://link.springer.com/chapter/10.1007/978-3-642-34704-7_5)
3. [https://link.springer.com/chapter/10.1007/978-3-662-45611-8_9](https://link.springer.com/chapter/10.1007/978-3-662-45611-8_9)
