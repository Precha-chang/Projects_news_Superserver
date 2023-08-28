# ระบบฐานข้อมูล
## ติดตั้ง `psycopg2` สำหรับการเชื่อมต่อไปยัง postgres SQL Server.
```
pip install psycopg2
```
## การตั้ังค่าการเชื่อมต่อฐานข้อมูลไปยัง postgres SQL Server. `settings.py`

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "<database name>",
        "USER": "<username>",
        "PASSWORD": "<password>",
        "HOST": "<host>",
        "PORT": "<port>",
    }
}
```
เปลี่ยนจากการเชื่อมต่อฐานข้อมูลแบบ Local เป็นระบบ Server

## ทำการ Migrate database เพื่อสร้างตารางทั้งหมดให้ฐานข้อมูลใหม่
```
python manage.py migrate
```

## Dump and Load database to JSON file.

เป็นการทำให้ข้อมูลในฐานข้อมูลอยู่ในรูปแบบ JSON เพื่อให้สามารถย้ายฐานข้อมูลได้


- ใช้สำหรับการโอนย้ายจากฐานข้อมูลเดิม ไปยังฐานข้อมูลใหม่


### คำสั่งสำหรับการ dumpdata และ loaddata

```

python manage.py dumpdata --exclude auth.permission --natural-foreign --indent 4 > db.json
```
*>>> ทำให้ข้อมูลอยู่ในรูปแบบ JSON*


### Loaddata to new database command.

```
python manage.py loaddata data.json
```
*>>> นำข้อมูลที่อยู่ในรูปแบบ JSON และ load ไปยังฐานข้อมูลใหม่*

