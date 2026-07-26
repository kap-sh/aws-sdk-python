"""Generated from Smithy shape ``com.amazonaws.healthlake#DeleteFHIRDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_id


class DeleteFHIRDatastoreRequest(TypedDict, closed=True):
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p> The AWS-generated identifier for the data store to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFHIRDatastoreRequest) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFHIRDatastoreRequest:
    out: DeleteFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("DeleteFHIRDatastoreRequest.datastore_id required")
    return out
