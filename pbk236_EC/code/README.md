HW8 README - Horisont chart (explanation)
======

Horisont plot - special type of plot, developed for multiple time series visualisation, quite popular in finances.
It is quite simple when you understand it: in order to prevent low values from falling into one line, we "fold" the plot N times (N is selected manually, in my case N=3), in other words we chop everything above max_value/N and put it down, and so on so forth N-1 times.

This way we visually "normalize" data, so it starts to be much more readable on the fly.  Unfortunately, I failed to find good
python implementation, so I decided to try make one.

##More on horisont charts
- [cubism](https://square.github.io/cubism/)
- [article](http://www.perceptualedge.com/articles/visual_business_intelligence/time_on_the_horizon.pdf)
