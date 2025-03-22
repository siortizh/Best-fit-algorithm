# (C)ontinuous (M)emory (A)lgorithms (cma)

## Best Fit Algorithm
This code implements a memory allocation simulator using the Best Fit algorithm. The program reads a file describing the available memory blocks and another file with memory requests. Then, it allocates memory to each request using the Best Fit algorithm and displays the memory status after each allocation.


Algorithm receives parameters:
   * `mem_avail`: a list of tuples, base and limit.
   * `req`: a size request for memory.
   * `index` position on the `mem_avail`. This is a circular index: `(index % len(mem_avail))`.

Possible values ​​of the algorithm: 

`None` if the
request cannot be fulfilled, or a quadruple:
   * `mem_avail`: a list of tuples of memory that are newly available (could be empty).
   * `base`: new base where the requested process start.
   * `limit`: new limit.
   * `index`: an index on the `mem_avail` where the request was found. If the
     memory were exhausted, the next valid position would be available.

### Requisitos
Python 3.x: Make sure you have Python installed on your system.

Dependencies: Install the required dependencies by running
```shell
pip install -r requirements.txt
```


## Test

First, set the `PYTHONPATH` variable replace (`<path-of-your-project`)
with your directory path.

Linux

```shell
export PYTHONPATH=$PYTHONPATH:<path-of-your-project>
```

Windows

```shell
SET PYTHONPATH=%PYTHONPATH%;<path-of-your-project>
```

Running the test.

```shell
python3 -m unittest test/test_basic_best_fit.py
```

```shell
python -m unittest test/test_basic_best_fit.py
```

## Execute cma simulator

First install click

```shell
python3 -m pip install click
```

```shell
python -p pip install click
```

To run the program

```shell
python3 cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt
```

```shell
python cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt
```


### To execute the best algorithm.

```shell
python3 cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --function best
```

```shell
python cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --function best
```


### To execute in different possition

```shell
python3 cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --pos 3
```

```shell
python cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --pos 3
```




