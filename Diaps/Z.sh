rm main.pdf
rm *.aux *.blg *.bbl *.log *.nav *.out *.xml *.snm *.toc
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
rm *.aux .blg *.bbl *.log *.nav *.out *.xml *.snm *.toc
evince main.pdf

