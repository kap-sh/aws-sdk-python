"""Generated from Smithy shape ``com.amazonaws.connectcases#LayoutSummary``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.layout_arn
    import aws_sdk_connectcases.types.layout_id
    import aws_sdk_connectcases.types.layout_name


class LayoutSummary(TypedDict):
    layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId"
    """<p>The unique identifier for of the layout.</p>"""
    layout_arn: "aws_sdk_connectcases.types.layout_arn.LayoutArn"
    """<p>The Amazon Resource Name (ARN) of the layout.</p>"""
    name: "aws_sdk_connectcases.types.layout_name.LayoutName"
    """<p>The name of the layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayoutSummary) -> dict:
    out: dict = {}
    out["layoutId"] = value["layout_id"]
    out["layoutArn"] = value["layout_arn"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> LayoutSummary:
    out: LayoutSummary = {}  # type: ignore[typeddict-item]
    if "layoutId" in data:
        out["layout_id"] = data["layoutId"]
    else:
        raise DeserializationError("LayoutSummary.layout_id required")
    if "layoutArn" in data:
        out["layout_arn"] = data["layoutArn"]
    else:
        raise DeserializationError("LayoutSummary.layout_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("LayoutSummary.name required")
    return out
