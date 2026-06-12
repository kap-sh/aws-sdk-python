"""Generated from Smithy shape ``com.amazonaws.connectcases#LayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.layout_id


class LayoutConfiguration(TypedDict):
    default_layout: NotRequired["aws_sdk_connectcases.types.layout_id.LayoutId"]
    """<p> Unique identifier of a layout. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LayoutConfiguration) -> dict:
    out: dict = {}
    if "default_layout" in value:
        out["defaultLayout"] = value["default_layout"]
    return out


def deserialize_json(data: dict) -> LayoutConfiguration:
    out: LayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "defaultLayout" in data:
        out["default_layout"] = data["defaultLayout"]
    return out
