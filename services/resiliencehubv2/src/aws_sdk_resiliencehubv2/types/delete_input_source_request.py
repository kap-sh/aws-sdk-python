"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteInputSourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.input_source_id


class DeleteInputSourceRequest(TypedDict):
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    input_source_id: "aws_sdk_resiliencehubv2.types.input_source_id.InputSourceId"
    """<p>The identifier of the input source to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInputSourceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["inputSourceId"] = value["input_source_id"]
    return out


def deserialize_json(data: dict) -> DeleteInputSourceRequest:
    out: DeleteInputSourceRequest = {}  # type: ignore[typeddict-item]
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError("DeleteInputSourceRequest.service_arn required")
    if "inputSourceId" in data:
        out["input_source_id"] = data["inputSourceId"]
    else:
        raise DeserializationError("DeleteInputSourceRequest.input_source_id required")
    return out
