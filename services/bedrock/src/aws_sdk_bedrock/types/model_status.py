"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ModelStatus: TypeAlias = Literal[
    "Active",
    "Creating",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Creating",
        "Failed",
    )
)


def serialize_json(value: ModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelStatus value: {data!r}")
    return cast(ModelStatus, data)
