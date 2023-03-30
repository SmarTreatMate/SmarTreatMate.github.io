<style>
.img-style {
  text-align: center;
}
  
.table-of-contents {
  position: fixed;
  left: 20px;
  width: 250px;
  padding: 10px;
  background-color: #a5c5ff;
  border: 2px solid #74b9ff;
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  color: #2c3e50;
  font-weight: bold;
}

.table-of-contents ul {
  padding-left: 20px;
}

.main-content {
  padding-left: 40px;
}

.separator {
  position: fixed;
  left: 280px;
  top: 80px;
  bottom: 0;
  border-left: 2px solid #74b9ff;
}
  
.custom-paragraph {
  color: #2d3436;
  text-align: justify;
}

.custom-paragraph::first-line {
  text-indent: 60px;
}

.custom-paragraph::first-letter {
  font-size: 21px;
  font-weight: normal;
}
</style>

<div class="table-of-contents">
  <p>Table of Contents</p>
  <ul>
    <li><a href="#abstract">Abstract</a></li>
    <li><a href="#survival_analysis">What is Survival Analysis?</a></li>
    <li><a href="#code-and-data">Code and Data</a></li>
    <li><a href="#how_to_use">How to use</a></li>
    <li><a href="#citation">Citation</a></li>
    <li><a href="#references">References</a></li>
  </ul>
</div>

<div class="separator"></div>

<div class="main-content">
<p id="name" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>Using Geographic Location-Based Public Health Features in Survival Analysis</strong></p>

<p class="custom-paragraph">&nbsp;&nbsp;This repository contains the code and data for the paper titled "Using Geographic Location-Based Public Health Features in Survival Analysis" by Navid Seidi, Ardhendu Tripathy, and Sajal Das.</p>


<p id="abstract" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>Abstract</strong></p>
<p class="custom-paragraph">&nbsp;&nbsp;Time elapsed till an event of interest is often modeled using the survival analysis methodology, which estimates a survival score based on the input features. There is a resurgence of interest in developing more accurate prediction models for time-to-event prediction in personalized healthcare using modern tools such as neural networks. Higher quality features and more frequent observations improve the predictions for a patient, however, the impact of including a patient's geographic location-based public health statistics on individual predictions has not been studied.
This paper proposes a complementary improvement to survival analysis models by incorporating public health statistics in the input features. We show that including geographic location-based public health information results in a statistically significant improvement in the concordance index evaluated on the Surveillance, Epidemiology, and End Results (SEER) dataset containing nationwide cancer incidence data. 
The improvement holds for both the standard Cox proportional hazards model and the state-of-the-art Deep Survival Machines model. 
Our results indicate the utility of geographic location-based public health features in survival analysis.</p>

  
<p id="survival_analysis" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>What is Survival Analysis?</strong></p>
<p class="custom-paragraph">&nbsp;&nbsp;The term "Survival Analysis" refers to a statistical methodology for the analysis of data, in which the outcome variable of interest is the probability of an <strong>Event</strong> occurring in each <strong>Time</strong> frame. By <strong>Time</strong>, we mean years, months, weeks, or days from the beginning of the follow-up of an individual until one of the desired events. Alternatively, time can refer to the age of an individual when an event occurs. Furthermore, by <strong>Event</strong>, we mean any change in the health status of an individual. This could be defined as disease incidence, relapse from remission, recovery (e.g., return to work), death, or any designated experience of interest that may happen to an individual <sup><a href="#SA">[1]</a></sup>.</p>
<p>
  This type of problem is distinct from a standard regression due to the <em>censoring of event times</em>. <strong>Censoring</strong> happens when we have some knowledge about an individual's survival period but do not know the precise survival time. As illustrated in Fig. <a href="#fig-censoring">1</a>, there are three types of censored data in any survival analysis study.
</p>
<ul>
  <li><strong>Right-censored:</strong> The event did not occur during the study, or the actual event time is equal to or greater than the observed survival time (p<sub>2</sub>, p<sub>3</sub> and p<sub>4</sub> in Fig. <a href="#fig-censoring">1</a>).</li>
  <li><strong>Left-censored:</strong> In some cases, "true survival time is less than or equal to the observed survival time" <sup><a href="#SA">[1]</a></sup>. It indicates that a person who is left-censored at time t has experienced an event between the beginning of time (time 0) and time t, but the exact timing of the event is unknown. In Fig. <a href="#fig-censoring">1</a> the event has been observed for p<sub>5</sub>, but the accurate time is not clear. The only known fact is that the event time is less than the time of ending the study.</li>
  <li><strong>Interval-censored:</strong> p<sub>6</sub> in Fig. <a href="#fig-censoring">1</a> has left the study sometime before the ending time and rejoined it again. Thus, it is impossible to make a comprehensive observation, and the actual event time is within a given time interval.</li>
</ul>

<div class="img-style">
<figure>
<img id="fig-censoring" src="https://raw.githubusercontent.com/SmarTreatMate/SmarTreatMate.github.io/main/survival%20analysis.png" alt="A description of the image" width="650" height="325">
<figcaption>Fig. 1. Various types of censoring in survival analysis.</figcaption>
</figure>
</div>
<p>For the analysis, we start by describing the Survival Function; the probability that a person will outlive a given period represented by S(t) as stated in equation (1). Moreover, equation (2) shows the Hazard Function, λ(t), which is the instantaneous probability per unit of the time that the event will occur:</p>

<p><em>Equation 1:</em></p>
<pre>
    S(t) = Pr(T > t)
</pre>

<p><em>Equation 2:</em></p>
<pre>
    λ(t) = lim(δ → 0) [Pr(t ≤ T < t + δ | T ≥ t) / δ]
</pre>

<p>Given that a person has survived up to time t, the hazard function is the probability that they will not survive an additional tiny period of time, δ. It indicates that those with a higher hazard value are at a greater risk of experiencing the event.</p>

<p>It is possible to construct these functions based on the most recent information regarding event occurrences, the event time for each individual in the datasets, and the related attributes associated with each unique patient. The above features are referred to as covariates and can be either Categorical or Numerical.</p>

<p>Although the survival function is theoretically a smooth curve, it is most commonly approximated using the Kaplan–Meier (K.M.) curve<sup><a href="#KM">[2]</a></sup> because of its simplicity. The Kaplan-Meier curve is a non-parametric method used to estimate the survival probability of a population over time based on censored data. It is commonly used to illustrate the estimated survival probability over time for a population or group of individuals. Kaplan–Meier curve is the most effective model whenever the covariate is categorical (e.g., medication vs. placebo) or when the covariate takes a small number of values (e.g., drug dosages 0, 20, 50, and 100 mg/day) that may be considered categorical. The K.M. curve is not as practical when dealing with quantitative factors such as gene expression, white blood cell count, or age. Cox proportional hazards regression analysis is an alternate approach when dealing with quantitative predictor variables. Moreover, the CoxPH model may be used with categorical predictor variables, which can be represented as dummy variables or as a binary indicator (0,1).</p>

<p>Let x<sub>i</sub> denote the vector features for individual i in the dataset. The hazard function for the Cox proportional hazards model is:</p>

<p><em>Equation 3:</em></p>
<pre>
    λ(t) = λ<sub>0</sub>(t) exp(β<sup>T</sup> x<sub>i</sub>)
</pre>

<p>where λ<sub>0</sub>(t) is defined as the baseline hazard function. β is a vector in the same dimension with x<sub>i</sub>. The Cox model may be modified if there is a reason to anticipate that the baseline hazard follows a certain shape. In this instance, the baseline hazard λ<sub>0</sub>(t) is substituted with a provided function. For example, if the baseline hazard function is a Weibull function of time, then it results in the 'Weibull proportional hazard model'<sup><a href="#Weibull">[3]</a></sup><sup><a href="#kumar1994proportional">[4]</a></sup>.</p>

<p id="code-and-data" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>Code and Data</strong></p>
<p class="custom-paragraph">&nbsp;&nbsp;The <code>code</code> directory contains the Python code used to generate the results in the paper. The <code>data</code> directory contains the datasets used in the analysis.</p>

<p id="how_to_use" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>How to use</strong></p>
<p class="custom-paragraph">&nbsp;&nbsp;To use the code, first clone the repository:</p>

<p id="citation" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>Citation</strong></p>
<p class="custom-paragraph">&nbsp;&nbsp;This project has been published in IEEE/ACM CHASE'23. The following is the citation:</p>


<p id="references" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>References</strong></p>
  <ol>
    <li id="SA">Kleinbaum, David G., and Mitchel Klein. Survival analysis a self-learning text. Springer, 1996.</li>
    <li id="KM">Kaplan, E. L., and Paul Meier. “Nonparametric Estimation from Incomplete Observations.” Journal of the American Statistical Association 53, no. 282 (1958): 457–81. https://doi.org/10.2307/2281868.</li>
    <li id="Weibull">Barrett, James. "Weibull-Cox proportional hazard model." Institute of Mathmatical and Molecular Biomedicine (2014): 1-7.</li>
    <li id="kumar1994proportional">Kumar, Dhananjay, and Bengt Klefsjö. "Proportional hazards model: a review." Reliability Engineering & System Safety 44, no. 2 (1994): 177-188.</li>
    <li id="ref2">Author B. (Year). Title of the book. Publisher.</li>
  </ol>
</div>
