"""Generated from Smithy shape ``com.amazonaws.lightsail#GetOperationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.non_empty_string


class GetOperationRequest(TypedDict):
    operation_id: "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    """<p>A GUID used to identify the operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOperationRequest) -> dict:
    out: dict = {}
    out["operationId"] = value["operation_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOperationRequest:
    out: GetOperationRequest = {}  # type: ignore[typeddict-item]
    if "operationId" in data:
        out["operation_id"] = data["operationId"]
    else:
        raise DeserializationError("GetOperationRequest.operation_id required")
    return out
