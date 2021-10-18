#!/bin/bash


python3 probability-integer-SIS.py < graph-star.in > graph-star.out && gnuplot -e "name='graph-star'" script-gnuplot-SIS.p && python3 probability-integer-SIS.py < graph-brasil.in > graph-brasil.out && gnuplot -e "name='graph-brasil'" script-gnuplot-SIS.p &&
python3 probability-integer-SIS.py < graph-cycle.in > graph-cycle.out && gnuplot -e "name='graph-cycle'" script-gnuplot-SIS.p && python3 probability-integer-SIS.py < graph-complete.in > graph-complete.out && gnuplot -e "name='graph-complete'" script-gnuplot-SIS.p &&
python3 probability-integer-SIS.py < graph-path.in > graph-path.out && gnuplot -e "name='graph-path'" script-gnuplot-SIS.p && python3 probability-integer-SIS.py < graph-wheel.in > graph-wheel.out && gnuplot -e "name='graph-wheel'" script-gnuplot-SIS.p &&
python3 probability-integer-SIS.py < graph-grid.in > graph-grid.out && gnuplot -e "name='graph-grid'" script-gnuplot-SIS.p
