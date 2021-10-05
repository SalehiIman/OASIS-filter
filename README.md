# OASIS-filter
## Open Affective Standardized Image Set (OASIS):
Open Affective Standardized Image Set (OASIS), is an open-access online stimulus set containing 900 color images depicting a broad spectrum of themes, including humans, animals, objects, and scenes, along with normative ratings on two affective dimensions—valence (i.e., the degree of positive or negative affective response that the image evokes) and arousal (i.e., the intensity of the affective response that the image evokes). The OASIS images, along with normative valence and arousal ratings, are available for download from www.benedekkurdi.com/#oasis. [^fn1]
## application:
While using affective image database, it would turn into a tedious work to find each peacture according to its normative ratings (affective dimensions like valence and arousal), listed in a information sheet. I wrote a code to do so without beeing required to select each picture individually; simply put, you can select the interval on a graph (fig1.depicting circumplex space  which would define your subcategory of images) and by selecting a folder, this code would copy all of those images to this folder as well as renaming them to your desirable list of names (e.g. f1,...,fn)
![plot](https://user-images.githubusercontent.com/48652270/136055798-84fb3cdd-4aa8-455f-b886-bd6c9baeb1c7.png)

## How to use it:
Run each file and follow 5 main steps described in figure-1.
<p align="center">
  <img width="600" height="400" src='https://user-images.githubusercontent.com/48652270/133934879-bda7673a-4ef6-4d06-8889-e66a56038b61.jpg'>
  <figcaption align="center">Fig.1 - Stages for selecting the limits of valence and arousal and select images from dataset based on the defined limits.</figcaption>
</p>

## To modify:
- change the caption for figure to : 'Image ratings in circumplex space, with valence (measured on a 1–7 Likert scale) on the x-axis and arousal (also measured on a 1–7 Likert
scale) on the y-axis'
- add another measure to categories based on person, object, . ..
- we neeed 2 versions of the code: 1- with **GUI** 2- without it 
[^fn1]: Kurdi B, Lozano S, Banaji MR. Introducing the Open Affective Standardized Image Set (OASIS). Behav Res Methods. 2017 Apr;49(2):457-470. doi: 10.3758/s13428-016-0715-3. PMID: 26907748.
