# Flask-Docs-and-Secrets-Check
Generate APIdocs in Flask simply by following the given code syntax which offcourse brings nice look to your app. It also checks for any possible secret that you may have forgotten to remove.


```
    _        ____                    ____       U  ___ u    ____    ____     
U  /"\  u  U|  _"\ u      ___       |  _"\       \/"_ \/ U /"___|  / __"| u  
 \/ _ \/   \| |_) |/     |_"_|     /| | | |      | | | | \| | u   <\___ \/   
 / ___ \    |  __/        | |      U| |_| |\ .-,_| |_| |  | |/__   u___) |   
/_/   \_\   |_|         U/| |\u     |____/ u  \_)-\___/    \____|  |____/>>  
 \\    >>   ||>>_    .-,_|___|_,-.   |||_          \\     _// \\    )(  (__) 
(__)  (__) (__)__)    \_)-' '-(_/   (__)_)        (__)   (__)(__)  (__)      


```
</br>

## Code Pattern
```
payLoad = {
        }
        return make_response(jsonify(payLoad), 200)
```

## Working
- write *#.n#* where n is number of payLoads in your route, at top of *@app.route('/')*
```
#.3.
# Your Comments maybe
@app.route("/login/google/callback")
@cross_origin(supports_credentials=True)
def callback():
  // code here
  // 3 payloads shall be present
```

## Usage
```
python APIdocs.py <directory/filename>
```

### [Example](https://github.com/D-E-F-E-A-T/AttendanceApp-Backend/tree/master/Guides)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![ForTheBadge built-with-swag](http://ForTheBadge.com/images/badges/built-with-swag.svg)](https://GitHub.com/D-E-F-E-A-T/) 

[![LinkedIn](https://img.shields.io/static/v1.svg?label=Connect&message=@Kush&color=grey&logo=linkedin&labelColor=blue&style=social)](https://www.linkedin.com/in/kush-choudhary-567b38169?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BDYkgbUGhTniMSRqOUkdN3A%3D%3D) [![Instagram](https://img.shields.io/badge/Instagram-follow-yellow.svg?logo=instagram&logoColor=white)](https://www.instagram.com/kush.philosopher/)
