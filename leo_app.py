import streamlit as st
import pandas as pd
import time as time

# 클럽 레어 관련 설명이 들어가야 함. 
st.title('Welcome to the LAZY LEO RARITY CALCULATOR!')
# 소개 링크
st.markdown("**About Lazy Leo Club Project:** [link](https://www.lazyleoclub.xyz/)")
# 계산 기준
st.markdown("**About the Rarity Standard:** [link](https://lazyleoclub.clubrare.xyz/the-standard-for-llc-rarity-tier)")
# 구매 링크
st.markdown("**Where to Adopt-a-Leo:** [link](https://opensea.io/collection/thelazyleoclub)")

# 모든 기준 로딩 실행
Back_set = pd.read_csv('Background.csv')
Body_set = pd.read_csv('Body.csv')
clothes_set = pd.read_csv('Clothes.csv')
eyes_set = pd.read_csv('Eyes.csv')
mouth_set = pd.read_csv('Mouth.csv')
mane_set = pd.read_csv('Mane.csv')
eye_acc_set = pd.read_csv('Eye_Accessories.csv')
face_acc_set = pd.read_csv('Face_Accessories.csv')
head_acc_set = pd.read_csv('Head_Accessories.csv')

# 1. get input attributes drop down - backgrounds 
background = st.selectbox('Backgrounds',['none','Light Green','Light Blue','Orange','Rose','Brown','Dark Green','Pink','Purple','Dark Blue','Maroon','Khaki','Blue','Light Gradient','Blue Electric','Green Yellow Gradient','Rose Orange Gradient','Green Purple Gradient', 'Gold Electric'])
t1 = Back_set.loc[Back_set['Trait'] == background ,'Score'].iloc[0]
t1p = Back_set.loc[Back_set['Trait']== background, 'Percentage'].iloc[0]
st.text('score:'+str(t1))
st.text('percentage:' + str(t1p))

# 2. get input attributes drop down - body
body = st.selectbox('Body',['none','Yellow','White','Green','Red','Light Green','Black','Ben Rocks','Flowers','Hell Boy','Skitties','Dalmatian','Thanos','Mumia','Panda','Gold'])
t2 = Body_set.loc[Body_set['Trait'] == body ,'Score'].iloc[0] 
t2p = Body_set.loc[Body_set['Trait']== body, 'Percentage'].iloc[0]
st.text('score:'+str(t2))
st.text('percentage:'+ str(t2p))

# 3. get input attributes drop down - Clothes
clothes =st.selectbox('Clothes',['none','Green Tshirt','Black Shirt','LightGreen Tshirt','Funny T-shirt','Bloody Shirt','Palmas Tshirt','Lion Tshirt','Purple Hudi','White Hudi','White Clothes','Orange Hudi','Back Hudi','Red Hudi','Green Hudi','LightBlue Hudi','Eth Shirt','Street Wear','I Love NY','Shirt With Chain','Rainbow Hudi','Summer','Track suit','Coat','Green LLC','Striped Longsleeve','LL Jacket','Tux','Brown Fashion','Formal Look','Black Fashion','Winter Suit','Safety Ballons','Red Striped Longsleeve','Superman','Prisoner','Safety Jacket',' Diving Suit'])
t3 = clothes_set.loc[clothes_set['Trait'] == clothes,'Score'].iloc[0] 
t3p = clothes_set.loc[clothes_set['Trait'] == clothes,'Percentage'].iloc[0] 
st.text('score:'+str(t3))
st.text('percentage:'+ str(t3p))

# # 4. get input attributes drop down - Eyes
eyes = st.selectbox('Eyes',['none','N/A','Neutral','Timid','Shy','Suspicious','Surprised','Creepy','Crying','Enthusiastic','Sad','Worried','Savage','Angry','Tear','Cute'])
t4 = eyes_set.loc[eyes_set['Trait'] == eyes,'Score'].iloc[0] 
t4p = eyes_set.loc[eyes_set['Trait'] == eyes,'Percentage'].iloc[0] 
st.text('score:'+str(t4))
st.text('percentage:'+ str(t4p))

# 5. get input attributes drop down - Mouth
mouth = st.selectbox('Mouth',['none','N/A','Base Smile','Cute Smile','Stressed','Smile','Vampire','Cute with nose','Base With Tooth','Surprised','Hunter','Mouth Opened','Ooops','With Tongue','Happy','Sad','Shy Expression'])
t5 = mouth_set.loc[mouth_set['Trait'] == mouth,'Score'].iloc[0] 
t5p = mouth_set.loc[mouth_set['Trait'] == mouth,'Percentage'].iloc[0]
st.text('score:'+str(t5))
st.text('percentage:'+ str(t5p))

# 6. get input attributes drop down - Mane
mane = st.selectbox('Mane',['none','Brown','Light Blue','White','Red','Rainbow','Wolverine Light Brown','Cruella','Wolverine Brown','Wolverine Orange','Snoop Dog','Wolverine Black','Wolverine Blue','Papaya','Pharaoh','Davy Jones','Rick','Gold'])
t6 = mane_set.loc[mane_set['Trait'] == mane,'Score'].iloc[0] 
t6p = mane_set.loc[mane_set['Trait'] == mane,'Percentage'].iloc[0] 
st.text('score:'+str(t6))
st.text('percentage:'+ str(t6p))

# 7. get input attributes drop down - Eye Accessories
eye_acc = st.selectbox('Eye Accessories',['none','Empty','Rayban Blue','Rayban White','Round Green','Meme','Round Blue','Button','Rayban Black','Round','Classic Round','Harry Potter','Monocle','Fashion Pink','Thin','Cyborg','Pink Round','Fashion','Fashion Orange','Fashion Green'])
t7 = eye_acc_set.loc[eye_acc_set['Trait'] == eye_acc,'Score'].iloc[0] 
t7p = eye_acc_set.loc[eye_acc_set['Trait'] == eye_acc,'Percentage'].iloc[0] 
st.text('score:'+str(t7))
st.text('percentage:'+ str(t7p))

# 8. get input attributes drop down - Face Accessories
face_acc = st.selectbox('Face Accessories',['none','N/A','Empty','Cyber Mask','Cyber Mask Dark','Doodle Mask','Gas Mask','Venom','Squid Mask','Cyber','Gum','Cyber Mask Gold'])
t8 = face_acc_set.loc[face_acc_set['Trait'] == face_acc,'Score'].iloc[0] 
t8p = face_acc_set.loc[face_acc_set['Trait'] == face_acc,'Percentage'].iloc[0] 
st.text('score:'+str(t8))
st.text('percentage:'+ str(t8p))

# 9. get input attributes drop down - Head Accessories
head_acc = st.selectbox('Head Accessories',['none','N/A','Panama Brown','Panama Red','Panama White','Airpods Max White','White Icecream','Airpods Max Red','Cap','Chaplin Green','Airpods Max Grey','Panama Blue','Halo','Airpods Max Blue','Ice cream','Saffari','Airpods Max Black','Chaplin','Panama Purple','Black Hat','TV','Unicorn','Panama Orange','Princess','Blue Fire','Pilot Hat','King','BrainDrain'])
t9 = head_acc_set.loc[head_acc_set['Trait'] == head_acc,'Score'].iloc[0]
t9p = head_acc_set.loc[head_acc_set['Trait'] == head_acc,'Percentage'].iloc[0]
st.text('score:'+str(t9))
st.text('percentage:'+ str(t9p))



# 결과 계산 버튼
if st.button ('Cacluate My Leo!'):
    with st.spinner(text='calculating...'):
        time.sleep(1)
        st.success('Congrats! your Total Leo Score is...')
    total_score = int(t1)+int(t2)+int(t3)+int(t4)+int(t5)+int(t6)+int(t7)+int(t8)+int(t9)
    # st.header('Congrats Your Total Leo Score is:')
    st.header(str(total_score))


st.text('From your Lazy Leo Club Korea Holder Community!')
st.markdown('**Errors?** report it in github [link](https://github.com/iksunglee/lazyleovaluator)')