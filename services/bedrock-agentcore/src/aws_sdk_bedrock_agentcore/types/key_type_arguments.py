"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#KeyTypeArguments``."""

from typing import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError


class KeyTypeArguments(TypedDict):
    text: "str"
    """<p>The text string to type. Maximum length: 10,000 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyTypeArguments) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> KeyTypeArguments:
    out: KeyTypeArguments = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    else:
        raise DeserializationError("KeyTypeArguments.text required")
    return out
