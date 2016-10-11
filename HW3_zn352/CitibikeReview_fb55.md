If your idea is that younger people take longer rides (not at least as long) the complement is shorter or equally long. So the = sign goed in the Null hypothesis, not in the alternative.


$H_0$ : $\frac{T_{\mathrm{tripduration}}}{N_{\mathrm{youngerpeople}}} &lt; \frac{T_{\mathrm{tripduration}}}{N_{\mathrm{elderpeople}}}$
$H_1$ : $\frac{T_{\mathrm{tripduration}}}{N_{\mathrm{youngerpeople}}} &gt;= \frac{T_{\mathrm{tripduration}}}{N_{\mathrm{elderpeople}}}$

these formulae are wrong:

you can write the average as
\bar{T_{\mathrm{tripduration}}}

or you can write out the formula for it as

\frac{\sum_{i=0}^{N_\mathrm{youngerpeople}}T_{\mathrm{tripduration},i}}{N_{\mathrm{youngerpeople}}}

but as you wrote it deviding T_{\mathrm{tripduration} by N does not mean what you want it to mean.

H_1 -> usually the notation is H_a

The data wrangling is not completed: you have not extracted the mean trip duration for ppl borned before and after 1970 (and stdev)

However you probably want to remove unlikely ages of >100 years of age (even >80) and trip durations = 0! Your data cleaning phase does not seem to be over.
Without that the test for correlation is meaningless



then you can proceed to a test of means (e.g. t-test)

