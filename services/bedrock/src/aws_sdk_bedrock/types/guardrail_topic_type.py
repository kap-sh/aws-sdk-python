"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailTopicType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailTopicType: TypeAlias = Literal["DENY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DENY",))


def serialize_json(value: GuardrailTopicType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailTopicType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailTopicType value: {data!r}")
    return cast(GuardrailTopicType, data)
