"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelModality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ModelModality: TypeAlias = Literal[
    "TEXT",
    "IMAGE",
    "EMBEDDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TEXT",
        "IMAGE",
        "EMBEDDING",
    )
)


def serialize_json(value: ModelModality) -> str:
    return value


def deserialize_json(data: str) -> ModelModality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelModality value: {data!r}")
    return cast(ModelModality, data)
