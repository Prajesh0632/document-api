import azure.functions as func
from database import get_db


def handle(req: func.HttpRequest) -> func.HttpResponse:
    nid_number = req.params.get("nid")

    if not nid_number:
        return func.HttpResponse("Missing nid", status_code=400)
    

    db = get_db()

    try:
        
        nid_collection = db.collection('nid-details')
        user_nid_data = nid_collection.document(nid_number).get()
        user_data_dict = user_nid_data.to_dict()
        

        return func.HttpResponse(user_data_dict["name"], status_code=200)
        
       
        


    except Exception as err:
        return func.HttpResponse(
            f"{err}",
            status_code=404,
        )

