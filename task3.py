import re


def normalize_phone(phone_number):
    pure = re.sub("[^\d]", "", phone_number)
    normalized = "+380"[0:13-len(pure)] + pure
    return normalized


numbers = ["067\\t123 4567", "(095) 234-5678\\n", "+380 44 123 4567", "380501234567", "    +38(050)123-32-34", "     0503451234", "(050)8889900", "38050-111-22-22", "38050 111 22 11   "]
for num in numbers:
    print(normalize_phone(num))
