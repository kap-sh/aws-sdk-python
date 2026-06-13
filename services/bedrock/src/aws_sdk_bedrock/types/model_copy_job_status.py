"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCopyJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ModelCopyJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
    )
)


def serialize_json(value: ModelCopyJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelCopyJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCopyJobStatus value: {data!r}")
    return cast(ModelCopyJobStatus, data)
