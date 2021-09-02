# Usage

Specify number of balls of each color as `-c` argument and total number of picked balls as `-t` argument. 

To evaluate run  
`python evaluate.py -c 2 3 4 7 -t 5`

To simulate run  
`python simulate.py -c 2 3 4 7 -t 5`

# Example

For example we have: 2 red, 3 green, 4 blue, and 7 purple balls, if we pick 5 by random we will have balls of all four colors with probability `0.230769` (`23.1%`), and only of one color with probability `0.004808` (`0.5%`).

```bash
python evaluate.py -c 2 3 4 7 -t 5
p(1) = 0.004808   0.5%
p(2) = 0.184295  18.4%
p(3) = 0.580128  58.0%
p(4) = 0.230769  23.1%

python simulate.py -c 2 3 4 7 -t 5
p(1) = 0.005   0.5%
p(2) = 0.184  18.4%
p(3) = 0.580  58.0%
p(4) = 0.231  23.1%
```

Note: evaluation for `t>10` will probably takes forever and all your memory.