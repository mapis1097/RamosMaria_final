grafica.py sigma.png solar.png:  datos.dat bayes.py fourier.py
	python bayes.py
	python fourier.py
	python grafica.py
	
datos.dat: tres.x
	./tres.x 
	./tres.x > datos.dat
tres.x : finitas.cpp
	c++ finitas.cpp -o tres.x
