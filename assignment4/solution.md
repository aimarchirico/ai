<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config"> MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });</script>

# Assignment 4

## Exercise 1

**a)**
Only (ii) and (iii) are correct based on the story.
Network (i) asserts that Wrapper and Shape are independent. However, the story says both Wrapper and Shape are determined by the Flavor. This makes them conditionally independent given Flavor, but not marginally independent. Network (iii) captures this relationship. Network (ii) is also capable of representing the distribution although it does not capture the conditional independence between Wrapper and Shape given Flavor.

**b)**
Network (iii) is the best representation.
The story describes a process where Flavor is determined first, and then Shape and Wrapper are determined based on that Flavor. Network (iii) mirrors this causal structure. It requires the fewest parameters and allows us to use the percentages given in the text directly as Conditional Probability Tables (CPTs).

**c)**
Yes. In network (i), there is no path between Wrapper and Shape, and they have no common ancestor. Therefore, the model asserts that $P(Wrapper, Shape) = P(Wrapper)P(Shape)$.

**d)**
To find $P(Red)$, we marginalize over Flavor ($F$):

$P(Red) = P(Red|Strawberry)P(Strawberry) + P(Red|Anchovy)P(Anchovy)$

Using the values:

$P(Strawberry) = 0.7$

$P(Anchovy) = 0.3$

$P(Red|Strawberry) = 0.8$

$P(Red|Anchovy) = 1 - 0.9 = 0.1$

$P(Red) = (0.8 \times 0.7) + (0.1 \times 0.3) = 0.56 + 0.03 = 0.59$

**e)**
We use Bayes' Rule:

$P(Straw|Red, Round) = \frac{P(Red, Round|Straw)P(Straw)}{P(Red, Round)}$

Because Wrapper and Shape are conditionally independent given Flavor:

$P(Red, Round|Straw) = P(Red|Straw) \times P(Round|Straw) = 0.8 \times 0.8 = 0.64$

$P(Red, Round|Anchovy) = P(Red|Anchovy) \times P(Round|Anchovy) = 0.1 \times 0.1 = 0.01$

Now find the denominator:

$P(Red, Round) = (0.64 \times 0.7) + (0.01 \times 0.3) = 0.448 + 0.003 = 0.451$

Final answer:

$P(Straw|Red, Round) = \frac{0.448}{0.451} \approx 0.9933$

**f)**
The expected value $E[V]$ is the sum of the values of the outcomes weighted by their probabilities:

$E[V] = s \cdot P(Strawberry) + a \cdot P(Anchovy)$

$E[V] = 0.7s + 0.3a$

## Exercise 2
**a)** Mary chooses the option with the highest Expected Utility $E[U]$.

$R = 500$

$U(x) = -e^{-x/500}$

Option 1 (Certainty):

$U(500) = -e^{-500/500} = -e^{-1} \approx -0.3679$

Option 2 (Lottery):

$E[U] = 0.6 \cdot U(5000) + 0.4 \cdot U(0)$

$E[U] = 0.6(-e^{-5000/500}) + 0.4(-e^{0})$

$E[U] = 0.6(-e^{-10}) - 0.4 \approx 0.6(-0.000045) - 0.4 \approx -0.400027$

Since $-0.3679 > -0.4000$, Mary chooses the $500 with certainty.

**b)** 
Indifference occurs when $U(100) = E[U_{lottery}]$:

$-e^{-100/R} = 0.5(-e^{-500/R}) + 0.5(-e^{0})$

$e^{-100/R} = 0.5 e^{-500/R} + 0.5$

Substitute $y = e^{-100/R}$

$y = 0.5y^5 + 0.5$

$y^5 - 2y + 1 = 0$

$R > 0 \implies y = e^{-100/R} <  1$

Solving $y^5 - 2y + 1 = 0$ for $y < 1$ gives $y \approx 0.51879$.

$e^{-100/R} = 0.51879$

$-100/R = \ln(0.51879)$

$R = \frac{-100}{-0.6562} \approx 152.39$

To three significant digits, $R = 152$.