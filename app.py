# Minds-eye.
import streamlit as st

# ==========================================
# 1. INITIALIZE GAME MEMORY (SESSION STATE)
# ==========================================
# This ensures the game remembers where the player is after every click
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'sub_stage' not in st.session_state:
    st.session_state.sub_stage = 'main' # Tracks if we are on the main question or the 'Plan B' backup question
if 'message' not in st.session_state:
    st.session_state.message = "" # Stores success/fail messages

def change_stage(new_stage):
    st.session_state.stage = new_stage
    st.session_state.level = 1
    st.session_state.sub_stage = 'main'
    st.session_state.message = ""
    st.rerun()

def fail_mission():
    st.session_state.stage = 'game_over'
    st.rerun()

def next_level():
    st.session_state.level += 1
    st.session_state.sub_stage = 'main'
    st.session_state.message = "Great job! Moving to the next level..."
    st.rerun()

# ==========================================
# 2. UI DESIGN & MAIN MENU
# ==========================================
st.title("🕵️‍♂️ The Mind's Eye")
st.divider()

if st.session_state.message:
    st.info(st.session_state.message)
    st.session_state.message = "" # Clear message after showing it once

if st.session_state.stage == 'intro':
    st.write("*Rain beats against the window. The phone on your desk rings... once, twice. You pick it up.*")
    st.write("**Mysterious Voice:** Listen closely. I need to know how your mind works.")
    st.write("**Mysterious Voice:** Which of these best describes your approach to solving a crisis?")
    
    st.write("---")
    if st.button("The Investigator: I read people and uncover the truth."):
        change_stage('investigator')
    if st.button("The Tech Architect: I code logic and rebuild networks."):
        change_stage('tech')

# ==========================================
# 3. PATH 1: THE INVESTIGATOR
# ==========================================
elif st.session_state.stage == 'investigator':
    st.subheader(f"Level {st.session_state.level}")
    
    if st.session_state.level == 1:
        if st.session_state.sub_stage == 'main':
            st.write("**Detective Vance:** Someone cleaned out the evidence locker.")
            st.write("- Alice said: 'I didn't open that locker.'")
            st.write("- Bob said: 'Charlie opened it.'")
            st.write("- Charlie said: 'Bob is a liar.'")
            st.write("**Exactly ONE of them is telling the truth. Who did it?**")
            
            ans = st.text_input("Name the culprit (Alice, Bob, Charlie):").strip().lower()
            if st.button("Submit Answer"):
                if ans == 'alice':
                    next_level()
                else:
                    st.session_state.sub_stage = 'plan_b'
                    st.rerun()
                    
        elif st.session_state.sub_stage == 'plan_b':
            st.warning("That didn't add up! Wait, she's making a run for it!")
            st.write("**Detective Vance:** Three cars speed out: Red, Blue, and Black. Red left before Blue. Black left before Red.")
            ans = st.text_input("Which car left FIRST? (Red, Blue, Black):").strip().lower()
            if st.button("Submit Backup Plan"):
                if ans == 'black':
                    next_level()
                else:
                    fail_mission()

    elif st.session_state.level == 2:
        if st.session_state.sub_stage == 'main':
            st.write("**Detective Vance:** She's running a betting ring. Payouts are: Match 1: 2k, Match 2: 4k, Match 3: 8k, Match 4: 16k.")
            ans = st.text_input("What is the payout for Match 5? (number only):").strip()
            if st.button("Submit Answer"):
                if ans == '32':
                    next_level()
                else:
                    st.session_state.sub_stage = 'plan_b'
                    st.rerun()
                    
        elif st.session_state.sub_stage == 'plan_b':
            st.warning("We missed the drop!")
            st.write("**Detective Vance:** The courier dropped an anagram for the backup spot: **R D P O**")
            ans = st.text_input("Unscramble the letters:").strip().upper()
            if st.button("Submit Backup Plan"):
                if ans == 'DROP':
                    next_level()
                else:
                    fail_mission()

    elif st.session_state.level == 3:
        st.success("🎉 You caught her! Investigator Path Complete!")
        if st.button("Play Again"):
            change_stage('intro')

# ==========================================
# 4. PATH 2: THE TECH ARCHITECT
# ==========================================
elif st.session_state.stage == 'tech':
    st.subheader(f"Level {st.session_state.level}")
    
    if st.session_state.level == 1:
        if st.session_state.sub_stage == 'main':
            st.write("**Sarah (via radio):** Malware tripped the breaker.")
            st.write("- Alpha MUST boot before Gamma.")
            st.write("- Do NOT boot Beta first.")
            st.write("- Gamma MUST boot before Beta.")
            
            ans = st.text_input("Type the first letter of each server in order (e.g., A B G):").strip().upper().replace(" ", "")
            if st.button("Boot Servers"):
                if ans == 'AGB':
                    next_level()
                else:
                    st.session_state.sub_stage = 'plan_b'
                    st.rerun()
                    
        elif st.session_state.sub_stage == 'plan_b':
            st.warning("Sequence shorted! Generator caught fire!")
            st.write("**Sarah:** Generator outputs exactly 150W. Load 1 is 50W. Load 2 is 100W.")
            ans = st.text_input("Plug in Load 1, Load 2, or BOTH?").strip().upper()
            if st.button("Balance Load"):
                if ans == 'BOTH':
                    next_level()
                else:
                    fail_mission()

    elif st.session_state.level == 2:
        if st.session_state.sub_stage == 'main':
            st.write("**Sarah:** Malware jumped to Port: 10, then 13, then 16, then 19.")
            ans = st.text_input("What port will it jump to next? (number):").strip()
            if st.button("Deploy Firewall"):
                if ans == '22':
                    next_level()
                else:
                    st.session_state.sub_stage = 'plan_b'
                    st.rerun()
                    
        elif st.session_state.sub_stage == 'plan_b':
            st.warning("Missed it! Override needed.")
            st.write("**Sarah:** What is the missing number: 5, 10, 15, ?")
            ans = st.text_input("Type the number:").strip()
            if st.button("Enter Password"):
                if ans == '20':
                    next_level()
                else:
                    fail_mission()

    elif st.session_state.level == 3:
        st.success("🎉 Systems secure! Tech Path Complete!")
        if st.button("Play Again"):
            change_stage('intro')

# ==========================================
# 5. GAME OVER SCREEN
# ==========================================
elif st.session_state.stage == 'game_over':
    st.error("❌ CRITICAL FAILURE. The timeline has collapsed.")
    st.write("You made a fatal error and the mission was lost.")
    
    if st.button("Rewind Timeline (Try Again)"):
        change_stage('intro')

