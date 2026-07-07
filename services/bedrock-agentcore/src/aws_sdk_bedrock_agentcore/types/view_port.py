"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ViewPort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.view_port_height
    import aws_sdk_bedrock_agentcore.types.view_port_width


class ViewPort(TypedDict, closed=True):
    width: "aws_sdk_bedrock_agentcore.types.view_port_width.ViewPortWidth"
    """<p>The width of the viewport in pixels. This value determines the horizontal dimension of the visible area. Valid values range from 800 to 1920 pixels.</p>"""
    height: "aws_sdk_bedrock_agentcore.types.view_port_height.ViewPortHeight"
    """<p>The height of the viewport in pixels. This value determines the vertical dimension of the visible area. Valid values range from 600 to 1080 pixels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewPort) -> dict:
    out: dict = {}
    out["width"] = value["width"]
    out["height"] = value["height"]
    return out


def deserialize_json(data: dict) -> ViewPort:
    out: ViewPort = {}  # type: ignore[typeddict-item]
    if "width" in data:
        out["width"] = data["width"]
    else:
        raise DeserializationError("ViewPort.width required")
    if "height" in data:
        out["height"] = data["height"]
    else:
        raise DeserializationError("ViewPort.height required")
    return out
