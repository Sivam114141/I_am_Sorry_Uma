import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Dil Se Sorry...",
    page_icon="❤️",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #FAFAFA;
    }
    .title-text {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        color: #B22222;
        margin-bottom: 0.2rem;
    }
    .subtitle-text {
        text-align: center;
        font-size: 1.3rem;
        font-weight: 600;
        color: #4A4A4A;
        margin-bottom: 1.5rem;
    }
    .card {
        background: #FFFFFF;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        border: 1px solid #F0E6E6;
        margin-bottom: 1.5rem;
        line-height: 1.8;
        font-size: 1.05rem;
        color: #333333;
    }
    .trust-section {
        background: #FFF8F8;
        border-left: 4px solid #B22222;
        padding: 1.2rem;
        border-radius: 4px;
        margin-top: 1rem;
        margin-bottom: 1.5rem;
        font-size: 0.98rem;
        color: #555555;
    }
    .comfort-card {
        background: #FFF9F2;
        border: 1px solid #FFE0B2;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1.2rem;
        color: #5D4037;
        line-height: 1.7;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2 = st.tabs(["💌 Apology & Promise", "✨ Why You Complete Me"])

with tab1:
    st.markdown('<div class="title-text">Dil Se Sorry...</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Meri jaan... ❤️</div>', unsafe_allow_html=True)

    # Main Message Card
    st.markdown("""
    <div class="card">
        <p>Mujhe pata hai maine tumhe hurt kiya. Ye soch ke bohot bura lagta hai.</p>
        <p>Tum mere liye kitne special ho, words mein nahi bata sakta.</p>
        <p>Jo bhi hua, uska koi excuse nahi. Maine galti ki aur main accept karta hoon.</p>
        <p>Tumhari feelings matter karti hain mujhe. Bohot zyada.</p>
        <p>Main promise karta hoon agli baar se zyada careful rahunga.</p>
        <p>Tum mujhe itna pyaar dete ho, aur maine tumhe takleef di. I'm really sorry.</p>
        <p style="font-weight: 600; color: #B22222;">Please mujhe ek aur chance do?</p>
    </div>
    """, unsafe_allow_html=True)

    # Trust Reflection Card
    st.markdown("""
    <div class="trust-section">
        <strong>Why your trust means everything to me:</strong><br>
        Trust takes time to build and just a moment to shake. I understand that words alone can't fix how you feel right now, but I want to earn back your confidence step by step. No deflecting, no excuses—just genuine effort and transparency moving forward.
    </div>
    """, unsafe_allow_html=True)

    # Interactive Response Buttons
    col1, col2 = st.columns(2)

    with col1:
        need_time = st.button("I need time, but I hear you 🕊️", use_container_width=True)

    with col2:
        forgive = st.button("I forgive you ❤️", use_container_width=True)

    # Dynamic feedback when she clicks "I need time"
    if need_time:
        st.markdown("""
        <div class="comfort-card">
            <h4 style="margin-top:0; color:#E65100;">Take all the time you need, meri jaan 🌸</h4>
            <p>Your peace of mind comes first. No pressure, no rush, and no expectations from my side right now.</p>
            <p>Even when you are upset with me, I want you to smile, drink some water, eat well, and know that you are deeply loved and respected.</p>
            <p style="margin-bottom:0;"><em>"I’m standing right here, waiting patiently whenever you feel ready to talk. Sending you the warmest hug."</em> 🫂✨</p>
        </div>
        """, unsafe_allow_html=True)

    if forgive:
        st.balloons()
        st.success("Thank you for your grace and your huge heart. I promise to cherish and protect our trust every single day. ❤️")

with tab2:
    st.markdown('<div class="title-text">You Complete Me</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle-text">Har pal tumhare saath special hai... ✨</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>Without you, everything feels a little incomplete and grey. You bring warmth, laughter, and calm into my life in ways you don't even realize.</p>
        <p>Tum sirf meri girlfriend nahi ho, meri sabse achhi dost aur meri comfort person ho. Hurting you hurts me from the inside because making you happy is always my real goal.</p>
        <p>I value us more than anything, and I never want to take you for granted ever again.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎵 A song that always reminds me of you")
    # Royalty-free romantic soft acoustic stream (or replace with any direct audio URL)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")
