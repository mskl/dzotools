# Digital Image Processing Homeworks
> Tools and submitted homeworks.


The project is hosted on the CTU gitlab as well as publicly on GitHub. To view the documentation and submitted homeworks I highly recommend using the generated documentation available at [https://mskl.github.io/fit-ni-dzo/](https://mskl.github.io/fit-ni-dzo/).

### Homework submissions
- [01: Monadic operations](https://mskl.github.io/fit-ni-dzo/monadic.html)
- [02: Fourier transform](https://mskl.github.io/fit-ni-dzo/fourier.html)
- [03: Convolution](https://mskl.github.io/fit-ni-dzo/convolution.html)
- [04: Bilateral filter](https://mskl.github.io/fit-ni-dzo/bilateral.html)
- [05: Gradient domain blending](https://mskl.github.io/fit-ni-dzo/image_blending.html)

```python
from dzotools.utils import imgload, arr2img

# To load the image into numpy array
arr = imgload(path="data/lenna.png")

# To draw the numpy array
arr2img(arr)
```




![png](docs/images/output_1_0.png)


