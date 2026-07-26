"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicType``."""

from typing import Literal, TypeAlias, cast

GuardrailTopicType: TypeAlias = Literal["DENY",]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailTopicType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicType:
    return cast(GuardrailTopicType, data)
