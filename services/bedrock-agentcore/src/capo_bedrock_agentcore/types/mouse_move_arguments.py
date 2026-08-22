"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MouseMoveArguments``."""

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError


class MouseMoveArguments(TypedDict, closed=True):
    x: "int"
    """<p>The target X coordinate on screen.</p>"""
    y: "int"
    """<p>The target Y coordinate on screen.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MouseMoveArguments) -> dict:
    out: dict = {}
    out["x"] = value["x"]
    out["y"] = value["y"]
    return out


def deserialize_json(data: dict) -> MouseMoveArguments:
    out: MouseMoveArguments = {}  # type: ignore[typeddict-item]
    if data.get("x") is not None:
        out["x"] = data["x"]
    else:
        raise DeserializationError("MouseMoveArguments.x required")
    if data.get("y") is not None:
        out["y"] = data["y"]
    else:
        raise DeserializationError("MouseMoveArguments.y required")
    return out
