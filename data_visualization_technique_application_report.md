# Technique Application Report: Time Series Analysis Dashboard

## Overall Dashboard
![Performance by gender and event type](F:\athletics_analysis\dashboard images\tsa1.png)
![Top 10 countries by performance through half-decades](F:\athletics_analysis\dashboard images\tsa2.png)


## Dashboard Context

This dashboard visualizes a reduced version of the World Athletics all-time rankings dataset. The analysis focuses on the three event types with the largest number of records: `middle-long`, `sprints`, and `jumps`. The main purpose is to support time-series analysis of athletic performance over history, compare gender-level performance trends, compare event-type trends, and identify historically strong countries.

The dashboard contains the following main components:

| Component | Visualization type | Main data source |
|---|---|---|
| KPI cards | Summary cards | `merge_total.csv` |
| Gender gap of performance through half-decades | Dumbbell chart | `fixed_gender_gap_dumbbell_chart_ready.csv` |
| Annual highest score by Gender | Line chart | `all_event_types_top_score_by_year_gender.csv` |
| Annual highest score by Event Type | Line chart | `all_event_types_top_by_year.csv` |
| Top 10 countries that had the best performance throughout history | Bump chart | `filled_bump_chart_top10_strength_ranked_by_half_decade_score.csv` |

The KPI cards summarize the dataset scope: around 297K records, 184 countries, 22K athletes, 24 events, top score of 1356, average age of 24.9, and an 88-year span.

## Chapter 1: Overview of Data Visualization

### Techniques / principles applied

- 1.2. Why data visualization
- 1.3. Role of data visualization
- 1.4. Types of data visualization

### How applied in the dashboard

The dashboard uses visualization to transform a large athletics dataset into interpretable time-based patterns. The raw dataset contains hundreds of thousands of records, so direct table inspection would not clearly reveal long-term trends, gender differences, or country dominance. The dashboard therefore uses charts and cards to summarize the data at multiple levels.

The dashboard combines exploratory and explanatory visualization. It is exploratory because slicers allow users to filter by `event_type` and inspect different groups. It is explanatory because each visual has a specific analytical message:

- The KPI cards provide the scope of the dataset.
- The gender gap dumbbell chart explains how men and women compare across half-decades.
- The annual line charts show performance progress over time.
- The bump chart explains country ranking changes through history.

This design supports the overall role of data visualization: reducing cognitive load, revealing patterns, and helping users compare performance across time, gender, event type, and country.

### Notes / adjustments

The dashboard does not attempt to visualize every event from the full Kaggle dataset. It focuses on the three largest event-type groups to keep the report coherent and avoid overwhelming the user.

## Chapter 2: Visual Models and Encoding

### Techniques / principles applied

- 2.1. Properties of data and measurement levels
- 2.2. Visual marks
- 2.3. Visual channels
- 2.4. Visual encoding

### How applied in the dashboard

The dashboard uses different encodings depending on the data type:

| Data field | Measurement type | Visual encoding |
|---|---|---|
| `year`, `half_decade_label` | Temporal / ordinal | X-axis or Y-axis order |
| `max_results_score`, performance score | Quantitative | Position on axis, line height, point location |
| `gender` | Nominal | Color and legend |
| `event_type` | Nominal | Slicer selection, line grouping |
| `nat` | Nominal | Color and line identity in bump chart |
| `rank_among_selected_top10` | Ordinal | Vertical rank position in bump chart |

In the two annual line charts, line marks encode temporal trends. The X-axis represents year, while the Y-axis represents the maximum result score. This is appropriate because line charts are effective for continuous time-series data.

In the gender gap dumbbell chart, point marks represent men and women scores for each half-decade. The horizontal distance between the points encodes the size of the gender gap. This is a clear encoding because users can compare both individual scores and the gap between them.

In the bump chart, each country is represented by a colored line. The vertical position encodes rank, while the horizontal axis encodes half-decade. This makes changes in country dominance visible over time.

The KPI cards use large numeric text marks. They are not designed to show trends, but to provide immediate summary context before users inspect the charts.

### Notes / adjustments

Color is used mainly for categorical separation. In the line chart by gender, red and blue distinguish men and women. In the bump chart, multiple colors distinguish countries. Because the bump chart has many categories, the legend is necessary, but the color load is higher than in the other charts.

## Chapter 3: Graphical Perception

### Techniques / principles applied

- 3.2. Magnitude estimation
- 3.3. Pre-attentive processing
- 3.4. Using multiple visual encodings
- 3.5. Gestalt grouping principles

### How applied in the dashboard

The dashboard prioritizes position-based encodings, which are generally easier to compare accurately than area or angle. In the line charts, users estimate performance score by vertical position. In the dumbbell chart, users estimate gender gap by horizontal distance. In the bump chart, users estimate country rank by vertical order.

Pre-attentive processing is applied through color and spatial grouping:

- Men and women are separated by color in the gender-based charts.
- Event type is controlled by slicers, reducing the number of visible series at once.
- KPI cards are placed in a single row at the top, so users immediately recognize them as overview metrics.
- Chart titles are placed directly above the relevant visual, supporting proximity and grouping.

Gestalt principles are visible in the layout. The top row of cards forms one group because of alignment and similarity. The two annual line charts are grouped on the right side of the first page. The dumbbell chart occupies the left side, visually separating gender-gap analysis from annual trend analysis.

### Notes / adjustments

The bump chart uses many colors, which can increase perceptual load. This is acceptable because the chart intentionally compares 10 countries over many half-decades, but it should be supported by a clear legend and event-type filtering.

## Chapter 4: Visualization for Multi-Dimensional Data

### Techniques / principles applied

- 4.1. Coordinate systems and axes
- 4.2. Visualizing amounts
- 4.4. Visualizing proportions
- 4.5. Visualizing relationships
- 4.6. Visualizing trends

### How applied in the dashboard

The dashboard visualizes multidimensional data by combining time, gender, event type, performance score, and nationality.

The KPI cards visualize amounts such as total records, total countries, total athletes, total events, top score, average age, and years span. These cards provide high-level quantitative context before the user reads the trend charts.

The gender gap dumbbell chart visualizes the relationship between gender and performance score across half-decades. It also indirectly shows whether men or women had the higher average top-score in each period. The horizontal layout is effective because the gap is encoded as distance between two points.

The Annual Highest Score by Gender line chart visualizes trends over time for men and women. It supports comparisons between gender trajectories within the selected event type. This chart is especially useful for detecting convergence, divergence, and periods of rapid performance improvement.

The Annual Highest Score by Event Type line chart visualizes the best annual result score for a selected event type. This shows how the peak performance level of an event group evolved over time.

The bump chart visualizes ranking relationships between countries over half-decades. It is not only a trend chart but also a rank-change visualization. It answers a different question from the line charts: not just "how high was the score?", but "which countries stayed dominant or moved up/down through history?"

### Notes / adjustments

Uncertainty is not explicitly visualized. The dashboard uses maximum scores and top-country ranks, so it emphasizes elite performance rather than confidence intervals or statistical uncertainty. This is acceptable for a descriptive sports-performance dashboard, but future work could include variability bands or record-count indicators.

## Chapter 6: Principles of Figure Design

### Techniques / principles applied

- 6.1. The principle of proportional ink
- 6.2. Handling overlapping points
- 6.3. Issues in the use of color
- 6.4. Multi-panel figures
- 6.5. Titles, captions, and tables
- 6.6. Balancing data and context
- 6.7. Problems with 3D charts

### How applied in the dashboard

The dashboard avoids 3D charts and uses mostly 2D position-based views. This follows the principle that 3D effects often distort perception without adding analytical value.

The KPI cards use large numbers and short labels. This balances data and context: users can quickly understand the dataset scale before interpreting detailed visualizations. The cards also use consistent sizes and alignment, making the page easier to scan.

The line charts use proportional axes and simple line marks. The visual ink mostly represents data rather than decoration. Gridlines are light, which helps users estimate values without dominating the chart.

The dumbbell chart is a good design choice for gender gap analysis because it avoids using two separate bar charts. The gap is visible as the distance between two points, so the chart directly supports the comparison task.

The bump chart is placed on a separate page because it requires more horizontal and vertical space than the other charts. This is a multi-panel design decision: instead of forcing all charts onto one crowded page, the dashboard separates country-ranking analysis from the main annual trend page.

Titles are descriptive and task-oriented:

- "Gender gap of performance through half-decades"
- "Annual highest score by Gender"
- "Annual highest score by Event Type"
- "Top 10 countries that have the best performance throughout history"

These titles tell the user what analytical question each chart answers.

### Notes / adjustments

The bump chart has potential overlap because 10 country lines can cross frequently. The dashboard handles this by limiting the chart to the top 10 countries and adding event-type filtering. This is a reasonable trade-off because showing all countries would make the chart unreadable.

## Chapter 8: Interactive Visualization

### Techniques / principles applied

- 8.2. Design principles
- 8.3. Interaction techniques: filtering, zooming, selection, view transformation
- 8.5. Tools and libraries
- 8.6. Practical applications

### How applied in the dashboard

The dashboard uses Power BI slicers to support interaction. The main interaction is filtering by `event_type`. This allows users to switch between `middle-long`, `sprints`, and `jumps` without needing separate dashboards for each event group.

The Annual Highest Score by Gender chart uses a dropdown slicer for `event_type`. This is effective because the chart only needs to show the selected event group, keeping the line chart compact and readable.

The Annual Highest Score by Event Type chart also uses an event-type slicer. This allows users to compare the temporal trajectory of each event type without placing all event-type lines on the same chart.

The gender gap dumbbell chart uses a list slicer for `event_type`. This lets users focus on one event type and inspect half-decade gender gaps more clearly.

The bump chart also uses an event-type slicer. This is important because the top 10 countries differ by event type. For example, top countries in `sprints` are not necessarily the same as top countries in `middle-long` or `jumps`.

### Notes / adjustments

The dashboard uses filtering rather than animation. This is appropriate because the goal is analytical comparison, not presentation animation. Filtering gives users control and prevents the page from becoming visually overloaded.

## Chapter 9: Storytelling with Data

### Techniques / principles applied

- 9.2. Fundamental principles of data storytelling
- 9.3. Visualization techniques for storytelling
- 9.4. Narrative styles in data storytelling
- 9.5. Interaction and exploration in storytelling

### How applied in the dashboard

The dashboard follows a clear analytical story:

1. Start with dataset scope using KPI cards.
2. Compare men and women through half-decades using the dumbbell chart.
3. Show annual peak performance trends by gender.
4. Show annual peak performance trends by event type.
5. Move to country-level historical dominance using the bump chart.

This structure moves from general to specific. The KPI cards provide context, the time-series charts show performance evolution, and the bump chart explains which countries were historically strongest.

The dashboard uses an interactive storytelling style. Users are not forced into a single fixed narrative. Instead, they can choose an event type and explore how the story changes across `middle-long`, `sprints`, and `jumps`.

The Country Strength Score supports the country-dominance story. It combines quality and coverage:

```text
country_strength_score = 0.8 * quality_percentile + 0.2 * coverage_percentile
```

This makes the country ranking more robust than ranking by one isolated peak performance. It rewards countries with high elite performance while still considering historical consistency.

### Notes / adjustments

The story focuses on elite performance because the main metrics are maximum result scores, top-10 countries, and top-5 average scores. This is appropriate for a World Athletics all-time ranking dashboard, but it should be described clearly so users do not interpret the dashboard as representing all athlete participation equally.

## Chapters Not Applied or Only Lightly Applied

### Chapter 5: Visualization for Graphs

This chapter is not central to the dashboard because the dataset is not modeled as a graph of nodes and edges. The bump chart shows ranked trajectories, but it is not a graph visualization in the network sense.

### Chapter 7: Map Visualization

Map visualization is not used in the current dashboard. Although the dataset contains country codes, the selected dashboard focuses on time-series trends and rankings rather than geographic distribution. A future extension could add a map to show country-level performance by region.

## Summary

The dashboard applies several key data visualization principles from the course. It uses line charts for time-series trends, a dumbbell chart for gender-gap comparison, a bump chart for country ranking changes, and KPI cards for fast contextual overview. The use of slicers supports interactive exploration while preventing the dashboard from becoming overcrowded. Overall, the design is appropriate for the analytical goal: explaining how elite athletics performance has changed over time across event types, genders, and countries.
