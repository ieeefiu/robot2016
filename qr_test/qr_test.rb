require 'zxing'
require 'opencv'

capture = OpenCV::CvCapture.open

puts ZXing.decode 'images/red.png'
puts ZXing.decode 'images/green.png'
puts ZXing.decode 'images/yellow.png'
puts ZXing.decode 'images/blue.png'
