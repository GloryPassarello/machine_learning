### Multiprocessing in Python


https://docs.python.org/3.4/library/multiprocessing.html?highlight=process

`multiprocessing` module has classes you can import specifically like

* Pool,
* Process,
* Queue,
* Pipe

#### Process

`from multiprocessing import Process`

It runs the function on a single process.

We initialize the process with for ex `p = Process(target=get_id)`
where `target` specifies the function we wish to call on a new process.
We then have to start the process `p.start()` and bring it back to our current process with `p.join()`.



The standard call for Process appears to be in the following if-statement:

      if __name__ == '__main__':
          p = Process(target=f)
          p.start()
          p.join()


#### Pool

`from multiprocessing import Pool`

The `Pool` class is similar to `Process` except that you can control a pool of processes.


        p2 = Pool()
        r2 = p2.apply_async(get_id_return)
        vals = r2.get()
        print "List of ids:", vals
        print "Parent id:", vals[0]
        print "Current id:", vals[1]

Another great use for Pool is its map which allows you to call the function many times, each on a new process.

        def f(x):
            r = x*2
            return r

        p4 = Pool()
        r4 = p4.map(f, [1,2,3])
        print r4



multiprocessing.Manager()