# DCF-Model
DCF model run by Python using data imported as csv.

The discounted cash flow formula is derived from the present value formula for calculating the time value of money
$DCF = \sum_{i = 1}^n \frac{CF_i}{(1 + r)^i} = \frac{CF_1}{(1 + r)^1} + \frac{CF_2}{(1 + r)^2} + \dots + \frac{CF_n}{(1 + r)^n}$
and compounding returns

$FV = DCF \cdot (1 + r)^n$

where
- $DPV$ is the discounted present value of the future cash flow $(FV)$, or $FV$ adjusted for the delay in receipt;
- $FV$ is the nominal value of a cash flow amount in a future period;
- $r$ is the interest rate or discount rate, which reflects the cost of tying up capital and may also allow for the risk that the payment may not be received in full;
- $n$ is the time in years before the future cash flow occurs.

$DPV = \int^T_0 FVe^{-\lambda t} dt = \int^T_0 \frac{FV(t)}{(1 + r)^t} dt$ where $FV(t)$ is the rate of cash flow, and $\lambda = \ln(1 + r)$. 
