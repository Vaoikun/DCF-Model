# DCF-Model
DCF model run by Python using data imported as csv.

$DCF = \sum^n_{i = 1} \frac{CF_i}{(1 + r)^i} = \frac{CF_1}{(1 + r)^1} + \frac{CF_2}{(1 + r)^2} + \dots + \frac{CF_n}{(1 + r)^n}$

$DPV = \int^T_0 FVe^{-\lambda t} dt = \int^T_0 \frac{FV(t)}{(1 + r)^t} dt$ where $FV(t)$ is the rate of cash flow, and $\lambda = \ln(1 + r)$. 
