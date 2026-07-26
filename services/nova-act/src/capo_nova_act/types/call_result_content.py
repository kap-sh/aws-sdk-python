"""Generated from Smithy shape ``com.amazonaws.novaact#CallResultContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_nova_act.errors import DeserializationError, SerializationError


class _CallResultContent_text(TypedDict, closed=True):
    text: "str"


CallResultContent: TypeAlias = _CallResultContent_text


# --- restJson1 ser/de ---
def serialize_json(value: CallResultContent) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("CallResultContent: no variant present")


def deserialize_json(data: dict) -> CallResultContent:
    if "text" in data:
        return {"text": data["text"]}
    else:
        raise DeserializationError("CallResultContent: no recognized variant key")
