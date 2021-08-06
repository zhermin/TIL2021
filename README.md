# TIL2021 (ML Hackathon on CV & SC)

---

## Competition Details
### Team Name: UT SamSan Tech

TIL was a Machine Learning hackathon hosted during DSTA's BRAINHACK event officially held from 22 June 2021 to 23 June 2021. However, the hackathon was split into 3 checkpoints. Prior to the official start of the event, Challenges 1 for both CV (Computer Vision) and SC (Sound Classification) were released in conjunction with their training materials. Challenges 2 and 3 were released on the first and second day respectively only if the mAP thresholds were crossed. 

The training and validation data for CV were animal photos in the COCO format while the SC data were 1 second audio clips of words spoken. mAP @ 0.50:0.95 (mean average precision) was used and the objective for CV was to correctly draw bounding boxes on all seen animals in the photos while for SC, it was to simply classify the correct word spoken. 

---

## Final Thoughts

Fresh out of a machine learning introductory module from Electrical Engineering, I was hoping to apply some of the knowledge onto this competition. Unfortunately, apart from understanding some of the jargons and the most basic of concepts such as regression, gradient descent and regularization, the module proved insufficient for the intense requirements of the competition. Thankfully, the training videos and basic CV/SC models were provided to get us started. 

It was also a little regrettable that I did not spend as much time on this competition before the 2 official days to maximise my learning and model training for Challenge 1 as I was caught up in another of BRAINHACK's event, CODE_EXP, an app hackathon. With that said, I think that even if I had more time, I might not have managed to catch up to the levels of some of the top teams in the competition, which I realised after watching their presentations. This was because I was mostly tweaking a few hyperparameters in the provided models, which honestly gave very little improvements and even caused me to fail the threshold required to receieve Challenge 3. This severely impacted my team's standings as the scores were 0 for Challenge 3's CV and SC portion. 

Overall, we ended up Rank 18 out of 60 groups in the senior category, with more teams in the junior category. It was an extremely interesting experience because it was my first time trying my hands on writing highly abstracted code from the help of the robust ML Python libraries instead of manually calculating matrices in my universty module. Moreover, the given data were sometimes pre-distorted to make it more challenging for models and hence, really tested us on a multitude of facets in ML, including my patience because my models were obviously under-optimized, leading to the occasional long training times. All in all, I would definitely join next year's hackathon though the clash in schedules with their other events might mean I have to prioritise the events better. 

---

## Final Leaderboards (18/60)
![SamSan Tech Ranking](https://zm-awsbucket.s3.ap-southeast-1.amazonaws.com/SamSan+Tech+-+Rank+18+out+of+60.jpg)