#!/bin/bash


python3 probability-integer-SIR.py < graph-star.in > graph-star.out && gnuplot -e "name='graph-star'" script-gnuplot.p && python3 probability-integer-SIR.py < graph-brasil.in > graph-brasil.out && gnuplot -e "name='graph-brasil'" script-gnuplot.p &&
python3 probability-integer-SIR.py < graph-cycle.in > graph-cycle.out && gnuplot -e "name='graph-cycle'" script-gnuplot.p && python3 probability-integer-SIR.py < graph-complete.in > graph-complete.out && gnuplot -e "name='graph-complete'" script-gnuplot.p &&
python3 probability-integer-SIR.py < graph-path.in > graph-path.out && gnuplot -e "name='graph-path'" script-gnuplot.p && python3 probability-integer-SIR.py < graph-wheel.in > graph-wheel.out && gnuplot -e "name='graph-wheel'" script-gnuplot.p &&
python3 probability-integer-SIR.py < graph-grid.in > graph-grid.out && gnuplot -e "name='graph-grid'" script-gnuplot.p