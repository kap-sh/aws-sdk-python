"""Generated from Smithy shape ``com.amazonaws.healthlake#DescribeFHIRDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_healthlake.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_healthlake.types.datastore_id


class DescribeFHIRDatastoreRequest(TypedDict, closed=True):
    datastore_id: "aws_sdk_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFHIRDatastoreRequest) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFHIRDatastoreRequest:
    out: DescribeFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
    if "DatastoreId" in data:
        out["datastore_id"] = data["DatastoreId"]
    else:
        raise DeserializationError("DescribeFHIRDatastoreRequest.datastore_id required")
    return out
