"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteInputSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.input_source_id


class DeleteInputSourceResponse(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    input_source_id: "aws_sdk_resiliencehubv2.types.input_source_id.InputSourceId"
    """<p>The identifier of the deleted input source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInputSourceResponse) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["inputSourceId"] = value["input_source_id"]
    return out


def deserialize_json(data: dict) -> DeleteInputSourceResponse:
    out: DeleteInputSourceResponse = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("DeleteInputSourceResponse.service_arn required")
    if "inputSourceId" in data:
        out["input_source_id"] = data["inputSourceId"]
    else:
        raise DeserializationError("DeleteInputSourceResponse.input_source_id required")
    return out
