"""Generated from Smithy shape ``com.amazonaws.bedrock#ModelCustomizationJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ModelCustomizationJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InProgress",
        "Completed",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_json(value: ModelCustomizationJobStatus) -> str:
    return value


def deserialize_json(data: str) -> ModelCustomizationJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ModelCustomizationJobStatus value: {data!r}"
        )
    return cast(ModelCustomizationJobStatus, data)
