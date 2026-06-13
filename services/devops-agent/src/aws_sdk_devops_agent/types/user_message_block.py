"""Generated from Smithy shape ``com.amazonaws.devopsagent#UserMessageBlock``."""

from typing import TypeAlias, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError


class _UserMessageBlock_text(TypedDict):
    text: "str"


class _UserMessageBlock_toolResult(TypedDict):
    toolResult: "object"


UserMessageBlock: TypeAlias = _UserMessageBlock_text | _UserMessageBlock_toolResult


# --- restJson1 ser/de ---
def serialize_json(value: UserMessageBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "toolResult" in value:
        return {"toolResult": value["toolResult"]}
    else:
        raise SerializationError("UserMessageBlock: no variant present")


def deserialize_json(data: dict) -> UserMessageBlock:
    if "text" in data:
        return {"text": data["text"]}
    elif "toolResult" in data:
        return {"toolResult": data["toolResult"]}
    else:
        raise DeserializationError("UserMessageBlock: no recognized variant key")
