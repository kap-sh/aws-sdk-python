"""Generated from Smithy shape ``com.amazonaws.bedrock#InputTags``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

InputTags: TypeAlias = Literal[
    "HONOR",
    "IGNORE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HONOR",
        "IGNORE",
    )
)


def serialize_json(value: InputTags) -> str:
    return value


def deserialize_json(data: str) -> InputTags:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputTags value: {data!r}")
    return cast(InputTags, data)
