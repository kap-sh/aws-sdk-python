"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#KeyPressArguments``."""

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError


class KeyPressArguments(TypedDict, closed=True):
    key: "str"
    """<p>The key name to press (for example, <code>enter</code>, <code>tab</code>, <code>escape</code>).</p>"""
    presses: NotRequired["int"]
    """<p>The number of times to press the key. Valid range: 1–100. Defaults to 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyPressArguments) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "presses" in value:
        out["presses"] = value["presses"]
    return out


def deserialize_json(data: dict) -> KeyPressArguments:
    out: KeyPressArguments = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("KeyPressArguments.key required")
    if "presses" in data:
        out["presses"] = data["presses"]
    return out
