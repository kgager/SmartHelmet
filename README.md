# SmartHelmet
LMU 2023 Capstone Project 

We are creating a smart bike helmet that can intelligently determine possible threats with computer vision. Using cameras embedded into the helmet, the helmet will receive a 360-degree video feed of a biker’s surrounding areas. This feed is sent to a computing board that will perform image processing on it to gain a high-level understanding of the surrounding area. The computing board will determine the location of captured people, cars, and potholes relative to the biker. The computing board will evaluate each of the identified objects to decide whether those objects are a threat or not. If the computing board decides an object is a threat, the computing board will send a signal to the biker’s phone. The signal that the phone receives will send another signal to the bikers’ headphones through a Bluetooth connection that will output an audible message warning the rider of the impending danger.  
	 A new dataset that the helmet was not trained on will be used to test its ability to intelligently determine possible threats. The reason for using an unfamiliar dataset is to test the helmet’s ability to detect new threats, not objects it has previously classified. We hope to achieve a validation accuracy of 90%. Validation accuracy is the accuracy of our model correctly identifying cars, humans, and potholes on a dataset that we did not use for training. Due to the heterogeneous nature of how potential threats can look, we can not expect to receive an accuracy of 100%. 
	This project will be useful as the product can mitigate the chance of a biker being in a dangerous situation. Furthermore, this project will promote a healthier, cleaner, and more sustainable mode of transportation as a more viable option.
	
To run the demo a user should
	Make sure their computer has a code editor and python 3 installed as well as access to a webcam
	Navigate to the GitHub project link: https://github.com/kgager/SmartHelmet
	Clone the repository
	Open up the project in a code editor
	Change the directory variable in the camera.py file found in the photoCapture folder to match the computer’s current directory
	Run python camera.py in the command line after navigating to the photoCapture folder
	
	After following these steps, the user will be able to see the program taking a photo and detecting the object from the captured image. Additionally, a user can also add their own test images to the source data folder. 
	
