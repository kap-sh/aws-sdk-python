"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CreateDatastoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_medical_imaging.types.datastore_id
    import aws_sdk_medical_imaging.types.datastore_status


class CreateDatastoreResponse(TypedDict, closed=True):
    datastore_id: "aws_sdk_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    datastore_status: "aws_sdk_medical_imaging.types.datastore_status.DatastoreStatus"
    """<p>The data store status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatastoreResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    import aws_sdk_medical_imaging.types.datastore_status

    out["datastoreStatus"] = (
        aws_sdk_medical_imaging.types.datastore_status.serialize_json(
            value["datastore_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateDatastoreResponse:
    out: CreateDatastoreResponse = {}  # type: ignore[typeddict-item]
    if "datastoreId" in data:
        out["datastore_id"] = data["datastoreId"]
    else:
        raise DeserializationError("CreateDatastoreResponse.datastore_id required")
    if "datastoreStatus" in data:
        import aws_sdk_medical_imaging.types.datastore_status

        out["datastore_status"] = (
            aws_sdk_medical_imaging.types.datastore_status.deserialize_json(
                data["datastoreStatus"]
            )
        )
    else:
        raise DeserializationError("CreateDatastoreResponse.datastore_status required")
    return out
