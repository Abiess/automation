
docker build -t qr-code-reader .
docker run -it --rm qr-code-reader

Alternative 

For linux: docker run -it --rm --device=/dev/video0 --privileged qr-code-reader


