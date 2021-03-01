# Digital Image Processing Homeworks
> Tools and submitted homeworks.


```python
from nbdev import *
```

The documentation should be automatically generated and hosted on github pages.

```python
from dzotools.monadic import imgload, arr2img

arr = imgload()
arr2img(arr)
```




![png](docs/images/output_2_0.png)



### Brightness

```python
from dzotools.monadic import brightness
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    <ipython-input-23-9cd6e7033402> in <module>
    ----> 1 from dzotools.monadic import brightness
    

    ImportError: cannot import name 'brightness' from 'dzotools.monadic' (/Users/matyas/dzotools/dzotools/monadic.py)

from dzotools.monadic import brightness

brightness(arr, 100)