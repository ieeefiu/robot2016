#!/usr/bin/env ruby
# qr_test.rb

require 'zxing'
require 'opencv'

include OpenCV

# initialize webcam
capture = CvCapture.open
# make a window for testing cam input
window = GUI::Window.new("qr test")

# capture and display image, decode and write result
puts "Press enter to capture"
readline
image = capture.query
image.save('test.jpg')
window.show(image)
puts ZXing.decode 'test.jpg'

# wait for a key press in image window
GUI::wait_key

# puts ZXing.decode 'images/red.png'
# puts ZXing.decode 'images/green.png'
# puts ZXing.decode 'images/yellow.png'
# puts ZXing.decode 'images/blue.png'
