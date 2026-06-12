"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DisplayContent``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apigatewayv2.types.__string_min1_max255
    import aws_sdk_apigatewayv2.types.__string_min1_max32768


class DisplayContent(TypedDict):
    body: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max32768.__stringMin1Max32768"
    ]
    """<p>The body.</p>"""
    title: NotRequired[
        "aws_sdk_apigatewayv2.types.__string_min1_max255.__stringMin1Max255"
    ]
    """<p>The title.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisplayContent) -> dict:
    out: dict = {}
    if "body" in value:
        out["body"] = value["body"]
    if "title" in value:
        out["title"] = value["title"]
    return out


def deserialize_json(data: dict) -> DisplayContent:
    out: DisplayContent = {}  # type: ignore[typeddict-item]
    if "body" in data:
        out["body"] = data["body"]
    if "title" in data:
        out["title"] = data["title"]
    return out
