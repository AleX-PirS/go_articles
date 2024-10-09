from pypdf import PdfReader
import regex as re

WORDS = ["Theme",
"Topic",
"Issue",
"Theory",
"Model",
"Principle",
"Aspect",
"Property",
"Feature",
"Characteristics",
"Characteristic",
"Characterize",
"Peculiarity",
"Peculiar",
"Specific ",
"Specifically",
"Unique",
"Common",
"Special",
"Specially",
"Particular particularly",
"Appropriate",
"Scope",
"Pattern",
"Sample",
"Way",
"Technique",
"Approach",
"Method",
"Methodology",
"Research",
"Study",
"Investigate",
"Investigation",
"Explore",
"Exploration",
"Analyse", 
"Analyze",
"Analysis ",
"Examine",
"Examination",
"Consider",
"Consideration",
"Considerable considerably",
"Account",
"Perspective",
"Prospect",
"Case",
"View",
"Significance",
"Significant",
"Insignificance",
"Insignificant",
"Essential essentially",
"Important",
"Current",
"Burning",
"Topical",
"Modern",
"Up-to-date",
"State-of-the-art",
"General",
"Generally",
"Identify ",
"Identification",
"Assess",
"Assessment",
"Estimate",
"Estimation",
"Discuss",
"Discussion ",
"Illustrate",
"Illustration",
"Demonstrate",
"Demonstration",
"Show",
"Exhibit",
"Perform",
"Performance",
"Carry out",
"Conduct",
"Calculate",
"Calculation",
"Compute",
"Computation",
"Measure",
"Measurement",
"Weigh",
"Weight",
"Derive",
"Derivation",
"Equal",
"Equation",
"Assume",
"Assumption",
"Find ",
"Findings",
"Support",
"Challenge",
"Provide",
"Provision",
"Affect",
"Effect",
"Include",
"Inclusion",
"Involve",
"Exclude",
"Exclusion",
"Develop",
"Development",
"Design",
"Classify",
"Classification",
"Establish",
"Establishment",
"Present",
"Presentation",
"Attempt",
"Explain",
"Explanation",
"Emphasise",
"Emphasize",
"Emphasis",
"Thesis",
"Hypothesis",
"Describe",
"Description",
"Relative",
"Relatively",
"Relevant",
"Abstract",
"Concrete",
"Complex",
"Quantitative",
"Qualitative",
"Accurate",
"Inaccurate",
"Rough",
"Roughly",
"Approximate",
"Approximation",
"Approximately",
"Precise",
"Precisely",
"Precision",
"Exactly",
"Apparent",
"Potential",
"Principal",
"Rigorous",
"Comparative", 
"Comparatively",
"Especially",
"Primary", 
"Primarily",
"Mainly",
"Mostly",
"Largely",
"Direct", 
"Directly",
"Indirect", 
"Indirectly",
"Frequent", 
"Frequently",
"Eventually",
"Ultimate", 
"Ultimately",
"Merely",
"Hardly ever",
"Possible", 
"Possibly",
"Probable", 
"Probably",
"Basically",
"Put forward",
"Make up", 
"Made up",
"Point out",
"Point up",
"Set out",
"Go into",
"Go through",
"Amount",
"Number",
"Substantial",
"Substantially",
"Deal with",
"Devoted to",
"Concern",
"Concerning",
"Few",
"A few",
"Little",
"A little",
"Occur",
"Occurrence",
"Refer to",
"Reference",
"Shed light on",
"In light of",
"Highlight",
"Crucial",
"Decisive",
"Sufficient",
"Preliminary",
"Preliminarily",
"Comprehensive",
"Comprehensively",
"Convenient",
"Contribute",
"Contribution",
"Evidence",
"Suggest",
"Propose",
"Offer",
"A great deal of",
"A wide range of",
"To … (some) extent",
"In a variety of ways",
"Aim",
"Purpose",
"Goal",
"Objective",
"Intend",
"In terms of",
"With respect to",
"With regard to",
"In respect of",
"Outline",
"Summary",
"Summarize",
"Obtain",
"Determine",
"Produce",
"Production",
"Create",
"Creation",
"Make use of",
"Extensive",
"Extensively",
"Careful",
"Carefully",
"Detailed",
"In detail",
"Thorough",
"Thoroughly",
"Remarkable",
"Striking",
"Consist in",
"Consist of",
"Contain",
"Comprise",
"Yield",
"Generate",
"Allow",
"Enable",
"Ensure",
"Permit",
"Modify", 
"Modification",
"Alter", 
"Alteration",
"Enhance", 
"Enhancement",
"Similar", 
"Similarly",
"Similarity ",
"Verify", 
"Verification",
"While",
"Whereas",
# "Since (=as)",
# "For (=as)",
"Initially",
"Finally",
"Following",
"Subsequently",
"Although",
"Despite",
"In spite of",
"Instead (of)",
"Nevertheless",
"On the contrary",
"In contrast",
"By contrast",
"On the one hand, on the other hand",
"Furthermore",
"Moreover",
"Due to",
"In order to",
"Hence",
"Therefore",
"Provided that",
"Unless",
]

def GetText(path:str) -> list[str]:
    data = list()
    for p in PdfReader(path).pages:
        data.append(p.extract_text().rstrip().replace("\n", "").replace(" -", "-").replace(" —", " — ").lower())
    return data

def FindWords(path):
    result = dict()
    res_w = []
    text = GetText(path)
    for w in WORDS:
        for idx, p in enumerate(text):
            # t = re.findall(rf" *[ a-zA-Z\-\–\,\:]*{w.lower()}[ a-zA-Z\-\–\,]*", p)
            t = re.findall(rf"[^\.]*{w.lower()}[^\.]*\.", p)
            if len(t)>0:
                if w in result:
                    result[w].append(t)
                else:
                    result[w] = t
                    res_w.append(w)
    for k, v in result.items():
        print(f"{k}|LEN={len(v)}: {v}")
    
    wordss = []
    for w in WORDS:
        if w not in list(result.keys()) and w not in wordss:
            wordss.append(w)

    print(f"\n\n\n----This article has:{len(res_w)}-----------------------")
    print(res_w)
    print(f"\n\n----Lasts:{len(wordss)}----------------------------------")
    print(wordss)

if __name__ == "__main__":
    FindWords("articles/SAR_100MS_90nm.pdf")