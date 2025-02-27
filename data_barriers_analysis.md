# Data Barriers Analysis

Based on the examination of the Federal Funds Rate, 1-Year Treasury Rate, and 10-Year Treasury Rate datasets, here are the key barriers identified and their impacts on descriptive statistics and data visualization:

## 1. Time Period Limitation (2015-onwards)

### Impact on Descriptive Statistics:
- Limited historical context for long-term trend analysis
- Reduced sample size affects statistical significance
- May not capture full economic cycles, leading to potential bias in mean and variance calculations

### Impact on Visualization:
- Shorter time series limits the ability to show long-term patterns
- May miss important historical reference points for comparison
- Could lead to misinterpretation of trends due to limited temporal scope

## 2. Different Scale Ranges Across Rates

### Impact on Descriptive Statistics:
- Federal Funds Rate: Values mostly < 1%
- 1-Year Treasury Rate: Values typically < 1%
- 10-Year Treasury Rate: Values typically > 1%

### Impact on Visualization:
- Challenges in creating meaningful comparisons on a single scale
- Risk of visual distortion when plotting multiple rates together
- May require separate axes or normalization, which can complicate interpretation

## 3. Monthly Aggregation Granularity

### Impact on Descriptive Statistics:
- Masks daily rate variations
- Smooths out extreme values
- May hide important short-term volatility

### Impact on Visualization:
- Less detailed representation of rate movements
- Could miss important intra-month patterns
- Might underrepresent market volatility

## 4. Discrete Time Intervals

### Impact on Descriptive Statistics:
- Step-wise changes rather than continuous progression
- Can affect calculation of rate changes and derivatives
- May impact correlation analyses between different rates

### Impact on Visualization:
- Creates "stepped" appearance in line plots
- May not accurately represent the continuous nature of rate changes
- Can make it harder to identify exact timing of rate changes
