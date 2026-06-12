"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionDefinition``."""

from typing import TypedDict

from aws_sdk_chatbot.errors import DeserializationError


class CustomActionDefinition(TypedDict):
    command_text: "str"
    """<p>The command string to run which may include variables by prefixing with a dollar sign ($).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionDefinition) -> dict:
    out: dict = {}
    out["CommandText"] = value["command_text"]
    return out


def deserialize_json(data: dict) -> CustomActionDefinition:
    out: CustomActionDefinition = {}  # type: ignore[typeddict-item]
    if "CommandText" in data:
        out["command_text"] = data["CommandText"]
    else:
        raise DeserializationError("CustomActionDefinition.command_text required")
    return out
