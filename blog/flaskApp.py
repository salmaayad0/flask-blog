from blog import create_app

app = create_app("development")
if __name__=='__main__':
     app.run(debug=True)
     

@app.errorhandler(404)
def page_not_found(error):
    return  f"<h1 style='color:red'> Enter A Valid Url </h1>"