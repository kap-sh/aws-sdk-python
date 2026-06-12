"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StopImportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.uuid


class StopImportRequest(TypedDict):
    import_id: "aws_sdk_cloudtrail.types.uuid.UUID"
    """<p> The ID of the import. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopImportRequest) -> dict:
    out: dict = {}
    out["ImportId"] = value["import_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopImportRequest:
    out: StopImportRequest = {}  # type: ignore[typeddict-item]
    if "ImportId" in data:
        out["import_id"] = data["ImportId"]
    else:
        raise DeserializationError("StopImportRequest.import_id required")
    return out
