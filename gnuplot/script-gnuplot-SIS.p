set term postscript color eps
set output name.'.eps'
set key outside
plot name.'.out' using 1:2 with points lw 2 title 'S', name.'.out' using 1:3 with points lw 2 title 'I'

