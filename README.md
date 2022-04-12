# Open Trailcam Pipes
Open Trailcam Pipes is a project that aims at providing **end-to-end open source pipelines** for downloading and processing images from low-cost connected trail cameras/camera traps.

Because such cameras often rely on SMTP protocol as for sending images and metadata, we aim at proposing a software package automating the downloading process from mailboxes compatible with the IMAP protocol, relieving users from a process that can be tedious in the case of time-series. We also want to take advantage of the metadata that is forwarded by the cameras, such as battery levels and temperature, which can be further plotted and mapped. 
To this end, we aim to provide a modular architecture that would allow this package to be used with multiple low-cost cameras brands.

We also aim at proving a modular solution to perform computer-vision tasks from these images, such as object identification and counting.
# Supported low cost cameras
- BSTCAM BST886 - [technical review on @codename5281's personal blog](https://www.lemotdejay.fr/la-vie-de-jay/frenesie-de-pieges-photographiques-partie-1-bst886-4g/) (in French)