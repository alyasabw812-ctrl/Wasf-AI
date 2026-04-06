import openai

class WasfAI_Engine:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_smart_description(self, product_name, category, features, tone="professional"):
        """
        خوارزمية توليد الوصف بناءً على القطاع التجاري ونبرة الصوت
        """
        # بناء "السياق" (Context) بناءً على المجال
        prompts = {
            "electronics": f"Focus on technical specs, durability, and innovation.",
            "fashion": f"Focus on style, comfort, trends, and emotional appeal.",
            "beauty": f"Focus on ingredients, skin benefits, and luxury feel.",
            "general": f"Focus on utility, price-value ratio, and problem-solving."
        }
        
        sector_context = prompts.get(category.lower(), prompts["general"])
        
        full_prompt = f"""
        Act as an expert e-commerce copywriter. 
        Product: {product_name}
        Category: {category}
        Features: {features}
        Tone: {tone}
        Guideline: {sector_context}
        Requirement: Write a persuasive product description using AIDA model (Attention, Interest, Desire, Action).
        Language: Arabic
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "أنت خبير تسويق رقمي متخصص في المتاجر الإلكترونية."},
                      {"role": "user", "content": full_prompt}]
        )
        
        return response.choices[0].message.content

# مثال لتشغيل الخوارزمية
# engine = WasfAI_Engine(api_key="YOUR_KEY")
# print(engine.generate_smart_description("ساعة ذكية", "electronics", "مقاومة للماء، بطارية 7 أيام"))
def client_dashboard_logic(user_input):
    """
    هذا الجزء يمثل 'لوحة التحكم' حيث يختار العميل إعداداته
    """
    settings = {
        "sector": user_input.get("sector"), # المجال: عقارات، تقنية، ملابس
        "target_audience": user_input.get("audience"), # الجمهور المستهدف
        "language_style": user_input.get("style"), # نبرة الصوت: فكاهي، رسمي، حماسي
    }
    return settings
    import requests

def verify_usdt_payment(wallet_address, expected_amount):
    """
    وظيفة للتحقق من وصول الدفع للمحفظة تلقائياً عبر TronGrid API
    """
    url = f"https://api.trongrid.io/v1/accounts/{wallet_address}/transactions/trc20"
    response = requests.get(url)
    
    if response.status_code == 200:
        transactions = response.json().get('data', [])
        for tx in transactions:
            # التحقق من القيمة والعملة (USDT)
            if tx['token_info']['symbol'] == 'USDT' and float(tx['value']) >= expected_amount:
                return True # الدفع تم بنجاح، افتح الخدمة للعميل
    return False
    
