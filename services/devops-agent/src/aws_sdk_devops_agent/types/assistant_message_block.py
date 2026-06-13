"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssistantMessageBlock``."""

from typing import TypeAlias, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError


class _AssistantMessageBlock_text(TypedDict):
    text: "str"


class _AssistantMessageBlock_toolUse(TypedDict):
    toolUse: "object"


AssistantMessageBlock: TypeAlias = (
    _AssistantMessageBlock_text | _AssistantMessageBlock_toolUse
)


# --- restJson1 ser/de ---
def serialize_json(value: AssistantMessageBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    elif "toolUse" in value:
        return {"toolUse": value["toolUse"]}
    else:
        raise SerializationError("AssistantMessageBlock: no variant present")


def deserialize_json(data: dict) -> AssistantMessageBlock:
    if "text" in data:
        return {"text": data["text"]}
    elif "toolUse" in data:
        return {"toolUse": data["toolUse"]}
    else:
        raise DeserializationError("AssistantMessageBlock: no recognized variant key")
