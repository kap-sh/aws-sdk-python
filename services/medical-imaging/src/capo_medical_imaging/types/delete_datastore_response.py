"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DeleteDatastoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.datastore_status


class DeleteDatastoreResponse(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    datastore_status: "capo_medical_imaging.types.datastore_status.DatastoreStatus"
    """<p>The data store status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatastoreResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    import capo_medical_imaging.types.datastore_status

    out["datastoreStatus"] = capo_medical_imaging.types.datastore_status.serialize_json(
        value["datastore_status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDatastoreResponse:
    out: DeleteDatastoreResponse = {}  # type: ignore[typeddict-item]
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("DeleteDatastoreResponse.datastore_id required")
    if "datastoreStatus" in data:
        import capo_medical_imaging.types.datastore_status

        out["datastore_status"] = (
            capo_medical_imaging.types.datastore_status.deserialize_json(
                data["datastoreStatus"]
            )
        )
    else:
        raise DeserializationError("DeleteDatastoreResponse.datastore_status required")
    return out
