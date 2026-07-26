"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MouseScrollArguments``."""

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError


class MouseScrollArguments(TypedDict, closed=True):
    x: "int"
    """<p>The X coordinate on screen where the scroll occurs.</p>"""
    y: "int"
    """<p>The Y coordinate on screen where the scroll occurs.</p>"""
    delta_x: NotRequired["int"]
    """<p>The horizontal scroll delta. Valid range: -1000 to 1000.</p>"""
    delta_y: NotRequired["int"]
    """<p>The vertical scroll delta. Valid range: -1000 to 1000. Negative values scroll down.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MouseScrollArguments) -> dict:
    out: dict = {}
    out["x"] = value["x"]
    out["y"] = value["y"]
    if "delta_x" in value:
        out["deltaX"] = value["delta_x"]
    if "delta_y" in value:
        out["deltaY"] = value["delta_y"]
    return out


def deserialize_json(data: dict) -> MouseScrollArguments:
    out: MouseScrollArguments = {}  # type: ignore[typeddict-item]
    if "x" in data:
        out["x"] = data["x"]
    else:
        raise DeserializationError("MouseScrollArguments.x required")
    if "y" in data:
        out["y"] = data["y"]
    else:
        raise DeserializationError("MouseScrollArguments.y required")
    if "deltaX" in data:
        out["delta_x"] = data["deltaX"]
    if "deltaY" in data:
        out["delta_y"] = data["deltaY"]
    return out
