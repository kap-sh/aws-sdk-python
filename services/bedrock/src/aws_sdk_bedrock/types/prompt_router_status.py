"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

PromptRouterStatus: TypeAlias = Literal["AVAILABLE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AVAILABLE",))


def serialize_json(value: PromptRouterStatus) -> str:
    return value


def deserialize_json(data: str) -> PromptRouterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PromptRouterStatus value: {data!r}")
    return cast(PromptRouterStatus, data)
