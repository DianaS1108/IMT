# A Unified Implementation of IMT

As part of my master's thesis, this repository contains the implementation of a series of iterative machine teaching (IMT) methods proposed in [Liu](https://wyliu.com/)'s line of work. We thus also provide a fair comparison of these different methods.

Specifically, the ipynb files contained in the ```src``` folder respectively implement:
- ```IMT```: [the baseline IMT method by sample selection](https://arxiv.org/abs/1705.10470)
- ```LAST```: [label synthesis teaching](https://arxiv.org/abs/2110.14432)
- ```DHT```: [data hallucination teaching](https://arxiv.org/abs/2210.17467)
- ```Joint```: a natural extension of the above methods that jointly synthesise label and input

For each of ```LAST```, ```DHT``` and ```Joint```, the method can be modified to a constrained version by commenting out/uncommenting few lines of code.

Besides these greedy methods, ```Parametrised``` implements the more challenging parametrised DHT trained using unrolling.

After setting up the environment with the light dependencies specified in ```requirements.txt```, the scripts can be easily run and will store their results in the ```results``` folder. The performance of difference methods can then be compared in ```plot.ipynb```.

The experiments here are based on [the half-moon dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html). We have generated and provided this simple demonstrative dataset in ```data``` for easy usage.
The codes can be adapted to use for other datasets with modifications.


## Acknowledgement
During the development of this project, we have referred to
- [Data Hallucination Teaching](https://github.com/Zeju1997/data_halucination_teaching)
- [Iterative Machine Teaching](https://github.com/Ipsedo/IterativeMachineTeaching)
