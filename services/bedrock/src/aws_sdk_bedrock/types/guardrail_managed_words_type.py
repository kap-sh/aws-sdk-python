"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailManagedWordsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailManagedWordsType: TypeAlias = Literal["PROFANITY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PROFANITY",))


def serialize_json(value: GuardrailManagedWordsType) -> str:
    return value


def deserialize_json(data: str) -> GuardrailManagedWordsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailManagedWordsType value: {data!r}")
    return cast(GuardrailManagedWordsType, data)
