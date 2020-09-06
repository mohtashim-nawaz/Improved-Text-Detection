# Text Detection in Distorted and Recaptured Images

Text Detection in images is a widely reserached area as it has a number of important applications. However, text detection in distorted and recaptured images has not been addressed much.

We created the largest available dataset of test images containing 126 distorted and 149 recaptured images to test various already available algorithms. It was found that none of the algorithms could perform satifactorily. 

We then analyzed the images in our dataset to find insights of the problem.

At last, we developed a few techniques and methods to improve the test detection in distorted and recaptured images. Although, the method is just preprocessing based, it performs considerable better than available methods.

We are in process of writing our findings as a report, link to which shall be published soon.

We found PSENet works best for our dataset images after transformation. So we recommend using PSENet as the final text detection algorithm.

### Requirements
- OpenCV
- Numpy
- Matplotlib
- Other general pyhton libarries

To test the images run the Testing Jupyter Notebook by passing the path to original images and number of images to be tested.

Link to dataset: [DATASET](https://drive.google.com/drive/folders/16CmJYDoa6PHEQ3pwfcdxYUJkKUlaFXUG?usp=sharing)
Github PSENet Repo:[PSENet Github](https://github.com/whai362/PSENet)
PSENet modified by us removing errors:[PSENet Modified](https://drive.google.com/drive/folders/1paZEOq8xzJwZ8Hk2n_CYEc7dfiw-DvDv?usp=sharing)

We thank PSENet developers and researchers for providing us an amazing algorithm.
