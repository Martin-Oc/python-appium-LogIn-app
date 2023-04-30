Instructions: 
● Design and implement a simple test automation framework for mobile automation
using any programming language for the given System under test and Test Case
written below depending on the device you personally own (choose Test Case for
ALT1 - Android or ALT2 - iPhone).
● Use appropriate design patterns.
● Ensure that you can run your test from a command line.
● Share your solution in a GitHub repository and send the link to office@qats.sk

I choose ALT1 Android application

Pre-requsit:
    Download native application Login App for Testing from Google Play store.

Test Case: 
    Login to SUT using username and password defined in application
    Assert successful login to the application
    Logout from SUT (Logout).
    Assert successful logout from the application



Pre-requisit to start test:
    Download Appium Server 1.15
    Android Studio 
        -device 'Pixel 5' 
        -API 33
        -download and install 'Login App for Testing' from Google Play store
    Python 3.11
    Visual Studio Code 

Start test:
    Run appium and start server 
        -Host: 0.0.0.0
        -Port 4723
    Start android studio 
    Start Pixel 5 Emulator
    Run in terminal command 'python3 tests/login-test.py'
