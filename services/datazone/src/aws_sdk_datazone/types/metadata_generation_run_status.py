"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

MetadataGenerationRunStatus: TypeAlias = Literal[
    "SUBMITTED",
    "IN_PROGRESS",
    "CANCELED",
    "SUCCEEDED",
    "FAILED",
    "PARTIALLY_SUCCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBMITTED",
        "IN_PROGRESS",
        "CANCELED",
        "SUCCEEDED",
        "FAILED",
        "PARTIALLY_SUCCEEDED",
    )
)


def serialize_json(value: MetadataGenerationRunStatus) -> str:
    return value


def deserialize_json(data: str) -> MetadataGenerationRunStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MetadataGenerationRunStatus value: {data!r}"
        )
    return cast(MetadataGenerationRunStatus, data)
