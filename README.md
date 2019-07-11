# ai_big_data_quantum_compution
SIGEVO -  inequality project

## CLASSIFICATION - NICK, WOJCIECH

## DRIFT VERIFICATION - YURI

DDM (Drift Detection Method) -> Estimates classifier error and standard deviation. Assumes that the convergence of the classifier decreases as more training examples arrive.If the classifier error still increases then there is a drift. 
  Learning with drift detection
  https://www.researchgate.net/profile/Joao_Gama3/publication/220974771_Learning_with_Drift_Detection/links/0912f50ace71293aed000000.pdf
  
EDDM (Early Drift Detection Method) -> is a modification of DDM
  Early drift detection method
  https://www.cs.upc.edu/~abifet/EDDM.pdf
 
Cumulative sum approach (CUSUM) ->  detects a change of a given parameter value of a probability distribution and indicates when the change is significant. WAT?
  Continuous inspection schemes
  https://www.jstor.org/stable/pdf/2333009.pdf?casa_token=38UW_CbPxWAAAAAA:ymVQZS_EhFbyvyOk9fZlo0XH-olWDuxhEQXAGMhGSMKYu7CA1ogAI1AP2-xQEfIVcgzqpgJKmxS3cCCga5anqoEf9NsUh0qHGsLd25JHWx7uCqbW-O8x

PageHinkley -> A modification of the CUSUM algorithm. The cumulative difference between observed classifier error and its average is taken into consideration. 
  A study on change detection methods
  https://www.researchgate.net/profile/Raquel_Sebastiao/publication/267231166_A_Study_on_Change_Detection_Methods/links/588a1980a6fdccb538f1ee1c/A-Study-on-Change-Detection-Methods.pdf
  
  ADWIN -> A window of incoming examples grows until identifying a change in the average value inside the window. Then it finds another window. Their split point between the 2 windoes is considered as an indication of concept drift.
  Learning from time-changing data with adaptive windowing
  https://www.cs.upc.edu/~GAVALDA/papers/adwin06.pdf
## NLP - BENJI


## RELATED WORKS - PENOUSAL
Fairer machine learning in the real world: Mitigating discrimination without collecting sensitive data 
https://journals.sagepub.com/doi/full/10.1177/2053951717743530

It shows that the problem persists, even after removing sensitive information
