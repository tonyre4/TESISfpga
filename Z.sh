# Borrar archivos intermedios...

rm *.aux
rm *.bbl
rm *.blg
rm *.loa
rm *.pdf
rm *.toc
rm *.log
rm *.lot
rm *.lof
rm *.lof


pdflatex tesis-UPV.tex
bibtex tesis-UPV
makeindex tesis-UPV.tex
pdflatex tesis-UPV.tex
pdflatex tesis-UPV.tex
evince tesis-UPV.pdf

