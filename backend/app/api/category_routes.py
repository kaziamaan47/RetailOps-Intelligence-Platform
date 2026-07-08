from fastapi import APIRouter


router = APIRouter(prefix="/categories", tags=["Service Categories"])


SERVICE_CATEGORIES = [
    {
        "id": 1,
        "name_en": "AC Repair and Service",
        "name_hi": "एसी रिपेयर और सर्विस",
        "name_mr": "एसी दुरुस्ती आणि सर्विस",
        "is_active": True,
        "subcategories": [
            {"id": 101, "name_en": "Installation", "name_hi": "इंस्टॉलेशन", "name_mr": "इंस्टॉलेशन"},
            {"id": 102, "name_en": "Gas Refill", "name_hi": "गैस रिफिल", "name_mr": "गॅस रिफिल"},
            {"id": 103, "name_en": "Water Leakage", "name_hi": "पानी लीक", "name_mr": "पाणी गळती"},
            {"id": 104, "name_en": "Annual Service", "name_hi": "वार्षिक सर्विस", "name_mr": "वार्षिक सर्विस"},
            {"id": 105, "name_en": "Not Cooling", "name_hi": "ठंडा नहीं हो रहा", "name_mr": "थंड होत नाही"},
            {"id": 106, "name_en": "General Inspection", "name_hi": "सामान्य जांच", "name_mr": "सामान्य तपासणी"},
        ],
    },
    {
        "id": 2,
        "name_en": "Electrician",
        "name_hi": "इलेक्ट्रीशियन",
        "name_mr": "इलेक्ट्रिशियन",
        "is_active": True,
        "subcategories": [],
    },
    {
        "id": 3,
        "name_en": "Plumbing",
        "name_hi": "प्लंबर",
        "name_mr": "प्लंबर",
        "is_active": True,
        "subcategories": [],
    },
]


@router.get("")
def list_categories():
    return {"categories": SERVICE_CATEGORIES}