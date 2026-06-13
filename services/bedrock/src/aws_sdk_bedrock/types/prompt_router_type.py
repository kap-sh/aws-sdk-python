"""Generated from Smithy shape ``com.amazonaws.bedrock#PromptRouterType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

PromptRouterType: TypeAlias = Literal[
    "custom",
    "default",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "custom",
        "default",
    )
)


def serialize_json(value: PromptRouterType) -> str:
    return value


def deserialize_json(data: str) -> PromptRouterType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PromptRouterType value: {data!r}")
    return cast(PromptRouterType, data)
