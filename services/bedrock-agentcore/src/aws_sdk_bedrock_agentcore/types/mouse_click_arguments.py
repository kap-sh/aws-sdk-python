"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MouseClickArguments``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.mouse_button


class MouseClickArguments(TypedDict):
    x: "int"
    """<p>The X coordinate on screen where the click occurs.</p>"""
    y: "int"
    """<p>The Y coordinate on screen where the click occurs.</p>"""
    button: NotRequired["aws_sdk_bedrock_agentcore.types.mouse_button.MouseButton"]
    """<p>The mouse button to use. Defaults to <code>LEFT</code>.</p>"""
    click_count: NotRequired["int"]
    """<p>The number of clicks to perform. Valid range: 1–10. Defaults to 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MouseClickArguments) -> dict:
    out: dict = {}
    out["x"] = value["x"]
    out["y"] = value["y"]
    if "button" in value:
        import aws_sdk_bedrock_agentcore.types.mouse_button

        out["button"] = aws_sdk_bedrock_agentcore.types.mouse_button.serialize_json(
            value["button"]
        )
    if "click_count" in value:
        out["clickCount"] = value["click_count"]
    return out


def deserialize_json(data: dict) -> MouseClickArguments:
    out: MouseClickArguments = {}  # type: ignore[typeddict-item]
    if "x" in data:
        out["x"] = data["x"]
    else:
        raise DeserializationError("MouseClickArguments.x required")
    if "y" in data:
        out["y"] = data["y"]
    else:
        raise DeserializationError("MouseClickArguments.y required")
    if "button" in data:
        import aws_sdk_bedrock_agentcore.types.mouse_button

        out["button"] = aws_sdk_bedrock_agentcore.types.mouse_button.deserialize_json(
            data["button"]
        )
    if "clickCount" in data:
        out["click_count"] = data["clickCount"]
    return out
