## **Background**

The data comes from an analytical chemistry technique called liquid chromatography (LC). Molecules in a mixture are pushed through a column and come out at different times. A molecule's **retention time** is how long it takes, and it depends on the molecule's physical and chemical properties.

The molecules here are **peptides**, short chains of **amino acids** (the building blocks of proteins). There are 20 standard amino acids, each with different properties such as size, charge, and hydrophobicity (how water- or fat-loving it is). A peptide is written as a string of letters, one per amino acid (for example `VALWNEVDGQTK`).

You are given peptide sequences and their measured retention times. It is already known publicly that retention time is largely driven by a peptide's hydrophobicity and size, and predictive models already exist. That is the starting point, not the goal.

## **What we're asking**

We want to see how you explore an unfamiliar dataset: the questions you ask of it, how you test your own assumptions, how you reason about what you find, how you leverage publicly available knowledge to guide your analysis. We are not grading predictive accuracy, and there is no hidden answer we are checking against - this is an open-ended exploration exercise.

A rough sense of where to begin:

1. **Understand the data.** Get to know the peptides and the measurements themselves, and form a view of what you are actually looking at and how far you would trust it.
2. **Then take it wherever you find it interesting.** You might dig into what actually drives retention behaviour, where the simple picture holds and where it breaks down, or what the data can and cannot tell you. The questions you ask, and what approaches you use, is up to you. We care about how you reason, not about reaching any particular result.

## **Deliverable**

Please share your work as a link to a GitHub repository containing your code and the reasoning behind it, presented so that someone else can follow what you did and why. Please include a README and ensure the code is reproducible with clear instructions. Please do not include the data, assume we already have it.

Please aim for about **two hours**, and strictly no more than that. This is deliberately more than you can finish in that time, and that is fine: **it is completely acceptable to stop partway and simply describe what you would do next - if relevant, please include these points in your write-up. We are interested in your thinking, not your coverage.**

Be ready to walk us through your work in an informal follow-up call.

## **Reference**

Peptide LC Retention Time Prediction, Kaggle. https://www.kaggle.com/competitions/peptide-lc-retention-time-prediction/overview
