"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SupportedLanguages``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

SupportedLanguages: TypeAlias = Literal["Python_3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Python_3",))


def serialize_json(value: SupportedLanguages) -> str:
    return value


def deserialize_json(data: str) -> SupportedLanguages:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupportedLanguages value: {data!r}")
    return cast(SupportedLanguages, data)
