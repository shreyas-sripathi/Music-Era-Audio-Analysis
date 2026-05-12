# Spotify 2025 vs. All-Time: Audio Feature Analysis

## Research Question
**How have the audio characteristics of hit songs changed between 2025 and the all-time most-streamed songs?**

## Hypothesis
Modern hit music (2025) would have higher danceability, energy, and tempo (BPM) compared to all-time classics.

## Methodology

### Data
- **2025 Hits**: Top 50 songs from Spotify Wrapped 2025 (n=50)
- **All-Time Classics**: Top 100 all-time most-streamed songs (n=100)
- **Features Analyzed**: Danceability, Energy, BPM, Valence, Acousticness

### Statistical Approach
1. **Descriptive Statistics**: Calculated means and standard deviations for each feature by era
2. **Visualization**: Box plots to compare distributions
3. **Hypothesis Testing**: Independent samples t-tests (α = 0.05)
4. **Effect Size**: Cohen's d to measure practical significance

## Key Findings

###  Statistically Significant Differences

**1. Danceability (p = 0.004, Cohen's d = 0.507)**
- 2025 Mean: 0.682
- All-Time Mean: 0.614
- **Difference**: 11% higher in 2025
- **Interpretation**: 2025 hits are significantly more danceable. This is a **medium effect size**, meaning the difference is practically meaningful.

**2. Valence (p = 0.003, Cohen's d = 0.519)**
- 2025 Mean: 0.666
- All-Time Mean: 0.551
- **Difference**: 21% higher in 2025
- **Interpretation**: 2025 hits are significantly more positive/upbeat. This is a **medium effect size**, suggesting modern hits prioritize optimistic, feel-good melodies and lyrics.

###  No Significant Differences

| Feature | p-value | Cohen's d | Conclusion |
|---------|---------|-----------|-----------|
| Energy | 0.683 | 0.071 | Not significant; negligible effect |
| BPM | 0.225 | -0.211 | Not significant; small effect |
| Acousticness | 0.964 | -0.008 | Not significant; negligible effect |

**Key Insight**: Energy levels and tempo have NOT changed meaningfully. Modern hits aren't faster or higher-energy—they're simply more groove-oriented and emotionally positive.

## Interpretation

The data reveals that **2025 hit production prioritizes groove and positivity over speed and intensity**.

### Business Implications
1. **For Producers**: Focus on danceability and positive melodies to create hits
2. **For Streaming Services**: Algorithm recommendations might prioritize upbeat, danceable tracks
3. **For Music Theory**: Modern hits balance energy with feel-good qualities

## Limitations
- Sample size is relatively small (50 + 100 songs)
- "All-time" songs span multiple decades; temporal trends may be confounded with production era
- Audio features are Spotify's proprietary metrics; exact algorithms unknown
- 2025 data represents only Wrapped rankings, which may have biases

## Conclusion
Modern Spotify hits (2025) are statistically significantly more danceable and positive than all-time classics, but not necessarily more energetic. This suggests a shift in production philosophy toward feel-good, groove-oriented music rather than high-intensity tracks.

---

## Files in This Analysis
- `spotify_combined_data.py` - Data loading and preparation
- `era_statistical_analysis.py` - Statistical tests and effect size calculations
- `spotify_era_analysis.png` - Publication figure
- `ANALYSIS.md` - This report