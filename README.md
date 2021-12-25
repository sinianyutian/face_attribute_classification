Implemented with tutorial: https://codelabs.developers.google.com/codelabs/recognize-flowers-with-tensorflow-on-android-beta/#0
and project: https://github.com/hoitab/TFLClassify

This app works with 5 types of face attributes and was trained on 1000 prepared images from celebA dataset for each attribute.

https://www.tensorflow.org/lite/guide/model_maker - used for train classification models.

* gender: male & female
loss: 0.2734 - accuracy: 0.9640

* hair: dark & pale
loss: 0.2693 - accuracy: 0.9793

* headdress: hat & no hat
loss: 0.2447 - accuracy: 0.9850

* eyeglasses: glasses & no glasses
loss: 0.3080 - accuracy: 0.9550

* pose: full face & rotated
loss: 0.3743 - accuracy: 0.8917

Currently the app works with frontal camera image.