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
  font-size: 22px;
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
<p class="custom-paragraph">&nbsp;&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

<img class="img-style" src="https://raw.githubusercontent.com/SmarTreatMate/SmarTreatMate.github.io/main/survival%20analysis.png" alt="A description of the image" width="650" height="325">


<p id="code-and-data" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>Code and Data</strong></p>
<p class="custom-paragraph">&nbsp;&nbsp;The <code>code</code> directory contains the Python code used to generate the results in the paper. The <code>data</code> directory contains the datasets used in the analysis.</p>

<p id="how_to_use" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>How to use</strong></p>
<p class="custom-paragraph">&nbsp;&nbsp;To use the code, first clone the repository:</p>

<p id="citation" style="background-color:#a5c5ff; padding: 10px; color:#2d3436; border-radius: 10px;"><strong>Citation</strong></p>
<p class="custom-paragraph">&nbsp;&nbsp;To use the code, first clone the repository:</p>
</div>
