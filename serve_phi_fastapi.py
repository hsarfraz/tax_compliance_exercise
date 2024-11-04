from fastapi import FastAPI, status
from fastapi.responses import PlainTextResponse, JSONResponse
from starlette.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"])


# FRONTEND
@app.get('/')
async def home():
    return PlainTextResponse('Upwork Tax Compliance Assignment.', status_code=status.HTTP_200_OK) 

@app.get("/checklist")
async def get_checklist( county:str, state:str):
    #params = request.query_params

    try:  
        # some JSON:
        point = {
            "title": "Business License Renewal",
            "description": "All businesses in Miami-Dade must renew their business licenses annually. This includes submitting renewal forms and paying applicable fees. Failure to comply may result in fines.",
            "due_date": "October 1st",
            "responsible_party": "Business Owner",
            "penalties": "Late renewals incur a 5% monthly penalty."
        }

        cp={"state ":state, 'county': county,"compliance_points": []}
        cp['compliance_points'].append(point)
        cp['compliance_points'].append(point)


        return JSONResponse(content=cp)
    except Exception as e:
        return PlainTextResponse(str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)        

if __name__ == "__main__":
   uvicorn.run("serve_phi_fastapi:app", host="0.0.0.0", port=5000, reload=False)