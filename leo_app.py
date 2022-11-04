import streamlit as st
import pandas as pd


# 클럽 레어 관련 설명이 들어가야 함. 
st.title('Welcome to the LAZY LEO RARITY CALCULATOR!')
# 소개 링크

# 구매 링크

# 프로필 링크 예시


# 모든 기준 로딩 실행
Back_set = pd.read_csv('Background.csv')
Body_set = pd.read_csv('Body.csv')
clothes_set = pd.read_csv('Clothes.csv')
eyes_set = pd.read_csv('Eye_Accessories.csv')
mouth_set = pd.read_csv('Mouth.csv')
mane_set = pd.read_csv('Mane.csv')
eye_acc_set = pd.read_csv('Eye_Accessories.csv')
face_acc_set = pd.read_csv('Face_Accessories.csv')
head_acc_set = pd.read_csv('Head_Accessories.csv')

# 1. get input attributes drop down - backgrounds 
background = st.selectbox('Backgrounds',['none','Light Green','Light Blue','Orange','Rose','brown','Dark Green','Pink','Purple','Dark Blue','Maroon','Khaki','Blue','Light Gradient','Blue Electric','Green Yellow Gradient','Rose Orange Gradient','Green Purple Gradient', 'Gold Electric'])


# 2. get input attributes drop down - body
body = st.selectbox('Body',['none','Yellow','White','Green','Red','Light Green','Black','Ben Rocks','Flowers','Hell Boy','Skitties','Dalmatian','Thanos','Mumia','Panda','Gold'])

# 3. get input attributes drop down - Clothes
clothes =st.selectbox('Clothes',['none','Green Tshirt','Black Shirt','LightGreen Tshirt','Funny T-shirt','Bloody Shirt','Palmas Tshirt','Lion Tshirt','Purple Hudi','White Hudi','White Clothes','Orange Hudi','Back Hudi','Red Hudi','Green Hudi','LightBlue Hudi','Eth Shirt','Street Wear','I Love NY','Shirt With Chain','Rainbow Hudi','Summer','Track suit','Coat','Green LLC','Striped Longsleeve','LL Jacket','Tux','Brown Fashion','Formal Look','Black Fashion','Winter Suit','Safety Ballons','Red Striped Longsleeve','Superman','Prisoner','Safety Jacket',' Diving Suit'])

# 4. get input attributes drop down - Eyes
eyes = st.selectbox('Eyes',['none','Neutral','Timid','Shy','Suspicious','Surprised','Creepy','Crying','Enthusiastic','Sad','Worried','Savage','Angry','Tear','Cute'])

# 5. get input attributes drop down - Mouth
mouth = st.selectbox('Mouth',['none','Base Smile','Cute Smile','Stressed','Smile','Vampire','Cute with nose','Base With Tooth','Surprised','Hunter','Mouth Opened','Ooops','With Tongue','Happy','Sad','Shy Expression'])

# 6. get input attributes drop down - Mane
mane = st.selectbox('Mane',['none','Brown','Light Blue','White','Red','Rainbow','Wolverine Light Brown','Cruelia','Wolverine Brown','Wolverine Orange','Snoop Dog','Wolverine Black','Wolverine Blue','Papaya','Pharaoh','Davy Jones','Rick','Gold'])

# 7. get input attributes drop down - Eye Accessories
eye_acc = st.selectbox('Eye Accessories',['none','Empty','Rayban Blue','Rayban White','Round Green','Meme','Round Blue','Button','Rayban Black','Round','Classic Round','Harry Potter','Monocle','Fashion Pink','Thin','Cyborg','Pink Round','Fashion','Fashion Orange','Fashion Green'])

# 8. get input attributes drop down - Face Accessories
face_acc = st.selectbox('Face Accessories',['none','Empty','Cyber Mask','Cyber Mask Dark','Doodle Mask','Gas Mask','Venom','Squid Mask','Cyber','Gum','Cyber Mask Gold'])

# 9. get input attributes drop down - Head Accessories
head_acc = st.selectbox('Head Accessories',['none','Panama Brown','Panama Red','Panama White','Airpods Max White','White Icecream','Airpods Max Red','Cap','Chaplin Green','Airpods Max Grey','Panama Blue','Halo','Airpods Max Blue','Ice cream','Saffari','Airpods Max Black','Chaplin','Panama Purple','Black Hat','TV','Unicorn','Panama Orange','Princess','Blue Fire','Pilot Hat','King','BrainDrain'])

# 결과 계산 버튼
st.button ('Cacluate My Leo!')

# 결과 점수

# 티어 등급 공유