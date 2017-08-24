# Pre step

## Install pdfmainer
	git clone https://github.com/euske/pdfminer.git
	python pdfminer/setup.py install

## Main repo
	git clone https://github.com/Sviatik/pdf-parse-py.git

## Convert pdf to xml examples:
	./tools/pdf2txt.py -p 2 -M 100 -W 1 -t xml ../pdf-parse-py/monitoring-and-diagnostics.pdf

