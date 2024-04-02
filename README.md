
docker build -t qr-code-reader .   --> bauen   
docker run -it --rm qr-code-reader  --> laufen lassen

Alternative 

For linux: docker run -it --rm --device=/dev/video0 --privileged qr-code-reader --> 


