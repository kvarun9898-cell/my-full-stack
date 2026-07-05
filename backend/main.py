@app.get("/version")
def version():
    return {
        "name": "Check whether the Backend is Running Successfully or not",
        "version": "v2"
    }
