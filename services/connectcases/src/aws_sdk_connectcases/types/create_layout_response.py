"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateLayoutResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.layout_arn
    import aws_sdk_connectcases.types.layout_id


class CreateLayoutResponse(TypedDict):
    layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId"
    """<p>The unique identifier of the layout.</p>"""
    layout_arn: "aws_sdk_connectcases.types.layout_arn.LayoutArn"
    """<p>The Amazon Resource Name (ARN) of the newly created layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLayoutResponse) -> dict:
    out: dict = {}
    out["layoutId"] = value["layout_id"]
    out["layoutArn"] = value["layout_arn"]
    return out


def deserialize_json(data: dict) -> CreateLayoutResponse:
    out: CreateLayoutResponse = {}  # type: ignore[typeddict-item]
    if "layoutId" in data:
        out["layout_id"] = data["layoutId"]
    else:
        raise DeserializationError("CreateLayoutResponse.layout_id required")
    if "layoutArn" in data:
        out["layout_arn"] = data["layoutArn"]
    else:
        raise DeserializationError("CreateLayoutResponse.layout_arn required")
    return out
