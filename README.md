# Geese Object Detection and Localization using Mask RCNN.

This repo is used to identify the geese in a video feed with the purpose of being used to scare geese off of my cousins lawn. **That's it, that's the tweet.**

The API used to do this object detection was the Mask-RCNN repository, linked [here](https://github.com/matterport/Mask_RCNN), and for information on how to install follow the link. The model was trained on Google Colab, of which a link will be provided after training as been done. There will be example footage of the detection working uploaded later on as well.

To run this, I suggest making an Anaconda environment with the requirements needed to run Mask RCNN.

To prepare the data, I follow [this tutorial for formatting the dataset](https://ersanpreet.wordpress.com/2018/08/17/creating-xml-file-for-custom-objects-object-detection-part-2/) and [this tutorial for creating the model.](https://machinelearningmastery.com/how-to-train-an-object-detection-model-with-keras/)
