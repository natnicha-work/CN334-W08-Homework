from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
products = [
        {"id": 1, "name": "Nappa small frame wallet", "price": 11000, "stock": 3},
        {"id": 2, "name": "Rigoberta Earring", "price": 4034, "stock": 150},
        {"id": 3, "name": "Huhsroom Charm", "price": 5500, "stock": 30},
    ]

comments = {
        1: [
            {"user": "por", "comment": "sooooo good"},
            {"user": "pan", "comment": "It's a waste of money"}
        ],
        2: [
            {"user": "por", "comment": "soso"},
        ]
    }

def user_view(request, username):
    user_data = {
    "por": {"email": "natnicha.chok@dome.tu.ac.th", "registered_date": "24-01-2025"},
    "pang": {"email": "amazee@gmail.com", "registered_date": "22-09-1997"},
    "pan": {"email": "pankhing@gmail.com", "registered_date": "13-06-2019"},
    }
    #ใส่เพื่อให้มันค้นหาผู้ใช้ที่กำหนถ้าไม่งั้นใส่ /user/[อะไรก็ได้] ก็จะขึ้นข้อมูล user ทั้งหมดเลยดลยต้องมี ถ้าไม่มี user ที่พิมพ์ไปก็ให้มัน error ไป
    if username in user_data:
        user_info= {"username": username, **user_data[username]}
        return JsonResponse(user_info)
    else:
        return JsonResponse({"error": "User not found"}, status=404)

def product_all_view(request):
    return JsonResponse({"products": products})
 
def product_by_id_view(request, id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return JsonResponse(product)
    return JsonResponse({"error": "Product not found"}, status=404)

def comments_by_product_id_view(request, id):
    return JsonResponse({"comments": comments.get(id, [])})

def summarize_view(request):
    return JsonResponse({
        "total_products": len(products),
        "total_orders": 2346,
        "total_comments": sum(len(c) for c in comments.values())
    })