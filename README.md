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
