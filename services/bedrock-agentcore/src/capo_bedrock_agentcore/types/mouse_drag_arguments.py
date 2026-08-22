"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MouseDragArguments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.mouse_button


class MouseDragArguments(TypedDict, closed=True):
    end_x: "int"
    """<p>The ending X coordinate for the drag.</p>"""
    end_y: "int"
    """<p>The ending Y coordinate for the drag.</p>"""
    start_x: "int"
    """<p>The starting X coordinate for the drag.</p>"""
    start_y: "int"
    """<p>The starting Y coordinate for the drag.</p>"""
    button: NotRequired["capo_bedrock_agentcore.types.mouse_button.MouseButton"]
    """<p>The mouse button to use for the drag. Defaults to <code>LEFT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MouseDragArguments) -> dict:
    out: dict = {}
    out["endX"] = value["end_x"]
    out["endY"] = value["end_y"]
    out["startX"] = value["start_x"]
    out["startY"] = value["start_y"]
    if "button" in value:
        import capo_bedrock_agentcore.types.mouse_button

        out["button"] = capo_bedrock_agentcore.types.mouse_button.serialize_json(
            value["button"]
        )
    return out


def deserialize_json(data: dict) -> MouseDragArguments:
    out: MouseDragArguments = {}  # type: ignore[typeddict-item]
    if data.get("endX") is not None:
        out["end_x"] = data["endX"]
    else:
        raise DeserializationError("MouseDragArguments.end_x required")
    if data.get("endY") is not None:
        out["end_y"] = data["endY"]
    else:
        raise DeserializationError("MouseDragArguments.end_y required")
    if data.get("startX") is not None:
        out["start_x"] = data["startX"]
    else:
        raise DeserializationError("MouseDragArguments.start_x required")
    if data.get("startY") is not None:
        out["start_y"] = data["startY"]
    else:
        raise DeserializationError("MouseDragArguments.start_y required")
    if data.get("button") is not None:
        import capo_bedrock_agentcore.types.mouse_button

        out["button"] = capo_bedrock_agentcore.types.mouse_button.deserialize_json(
            data["button"]
        )
    return out
