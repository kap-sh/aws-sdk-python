"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelImportJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ModelImportJobStatus: TypeAlias = Literal[
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


def serialize_json(value: ModelImportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelImportJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelImportJobStatus value: {data!r}")
    return cast(ModelImportJobStatus, data)
