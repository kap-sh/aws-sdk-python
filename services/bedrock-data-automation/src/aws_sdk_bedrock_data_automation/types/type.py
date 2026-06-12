"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_data_automation.errors import DeserializationError

"""Type"""
Type: TypeAlias = Literal[
    "DOCUMENT",
    "IMAGE",
    "AUDIO",
    "VIDEO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOCUMENT",
        "IMAGE",
        "AUDIO",
        "VIDEO",
    )
)


def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Type value: {data!r}")
    return cast(Type, data)
