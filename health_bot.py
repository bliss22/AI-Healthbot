import streamlit as st
from googletrans import Translator




# Simulated Chatbot Responses 
def simulated_gpt_response(question, intent):
    question = question.lower()

    # NUTRITION INTENT
    if intent == "nutrition":
        if "hemoglobin" in question or "iron deficiency" in question:
            return (
                "To boost hemoglobin, include iron-rich foods like spinach, beetroot, pomegranate, dates, lentils, and red meat. "
                "Vitamin C (from citrus fruits) improves iron absorption."
            )
        elif "dengue" in question or "platelet" in question:
            return (
                "For dengue recovery, focus on hydration with coconut water, fruit juices, and soups. "
                "Papaya leaf extract and kiwi may support platelet production."
            )
        elif "cholesterol" in question:
            return (
                "Avoid saturated fats (like butter, red meat) and fried foods. "
                "Eat oats, nuts, fatty fish, and increase fiber to reduce bad cholesterol."
            )
        elif "lactose" in question or "milk" in question:
            return (
                "People with lactose intolerance should avoid regular milk and opt for lactose-free alternatives like almond or soy milk."
            )
        elif "coffee" in question and "iron" in question:
            return (
                "Avoid coffee or tea right before or after iron-rich meals, as they reduce iron absorption."
            )
        elif "immunity" in question:
            return (
                "To improve immunity, eat a balanced diet rich in fruits, vegetables, vitamin C, zinc (pumpkin seeds), and get enough sleep."
            )
        elif "gain weight" in question:
            return (
                "To gain weight healthily, eat calorie-dense yet nutritious foods like nuts, avocados, whole grains, and lean proteins. Avoid junk food."
            )
        elif "lose weight" in question:
            return (
                "For healthy weight loss, focus on portion control, whole foods, fiber, and regular physical activity. Avoid crash diets."
            )
        elif "kidney" in question or "renal" in question:
            return (
                "Kidney patients may need to reduce protein, potassium, sodium, and phosphorus intake. Consult a renal dietitian for a personalized plan."
            )
        elif "calories" in question and "diabetic" in question:
            return (
                "Calorie needs vary, but diabetic individuals should follow a balanced diet with controlled carbs, fiber, and lean proteins. "
                "Consult a nutritionist for an exact plan."
            )
        else:
            return (
                "Eat a balanced diet with plenty of vegetables, fruits, whole grains, lean proteins, and stay hydrated. "
                "Let me know if you have a specific health concern!"
            )

    # MEDICINE INTENT
    elif intent == "medicine":
        if "paracetamol" in question and "pregnancy" in question:
            return "Paracetamol is generally considered safe during pregnancy, but it should be taken only if necessary and after consulting your doctor."
        elif "ibuprofen" in question:
            return "Avoid taking ibuprofen on an empty stomach, as it may cause irritation. Take it after food or milk."
        elif "cetirizine" in question:
            return "Cetirizine can be taken once daily for allergies, but prolonged use should be under a doctor’s advice."
        else:
            return "Always follow your doctor's advice before taking any medication, especially if you have existing health conditions."

    # EMERGENCY INTENT
    elif intent == "emergency":
        if "heart attack" in question:
            return "Call emergency services immediately. Chew one aspirin (if not allergic) and try to stay calm while waiting for help."
        elif "bleeding" in question:
            return "Apply firm pressure to the wound, keep the person calm, and elevate the area if possible. Seek medical help if it doesn't stop."
        elif "faint" in question or "unconscious" in question:
            return "Lay the person flat, elevate their legs, and loosen any tight clothing. If they don't regain consciousness quickly, call emergency services."
        else:
            return "In any emergency, it's best to stay calm and call for professional medical help immediately."

    # GENERAL INTENT
    else:
        if "water" in question:
            return "Most adults should aim for 2–3 liters of water a day, but needs vary depending on climate, activity, and health conditions."
        elif "breakfast" in question:
            return "Skipping breakfast regularly may slow metabolism and lead to overeating later. A healthy breakfast supports energy levels and weight management."
        else:
            return "I'm here to help with general health advice. Ask me about diet, medicine safety, or what to do in emergencies."

# Intent classification logic
def classify_intent(question):
    nutrition_keywords = ['eat', 'food', 'diet', 'drink', 'nutrition', 'hemoglobin','fruits']
    medicine_keywords = ['tablet', 'medicine', 'safe', 'take', 'paracetamol', 'ibuprofen', 'dose', 'pregnancy']
    emergency_keywords = ['emergency', 'bleeding', 'heart attack', 'accident', 'cpr','faints','fainting']

    question_lower = question.lower()

    if any(kw in question_lower for kw in emergency_keywords):
        return 'emergency'
    elif any(kw in question_lower for kw in medicine_keywords):
        return 'medicine'
    elif any(kw in question_lower for kw in nutrition_keywords):
        return 'nutrition'
    else:
        return 'general'

# Translate to English (for other language input)
def translate_to_english(text):
    translator = Translator()
    translated = translator.translate(text, src='auto', dest='en')
    return translated.text

# Streamlit Interface
st.set_page_config(page_title="HealthBot", page_icon="🩺")
st.title("🩺 Health AI Chatbot")
st.markdown("Ask me any health-related question (English/ Hindi/ Tamil).")

user_input = st.text_input("Your Question")

if user_input:
    # Detect language and translate if not English
    translator = Translator()
    detected_lang = translator.detect(user_input).lang
    original_text = user_input
    if detected_lang != 'en':
        user_input = translate_to_english(user_input)
        st.markdown(f"🔄 Translated to English: *{user_input}*")

    # Step 1: Classify intent
    intent = classify_intent(user_input)
    st.markdown(f"🧠 Detected Intent: `{intent}`")

    # Step 2: Simulate GPT or use API
    answer = simulated_gpt_response(user_input, intent)

    # (Optional) Translate answer back
    if detected_lang != 'en':
        answer = translator.translate(answer, src='en', dest=detected_lang).text

    # Step 3: Display
    st.markdown("### 💬 Response:")
    st.success(answer)

    st.caption("Note: This is not medical advice. Please consult a doctor for emergencies.")
