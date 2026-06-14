"""Generated from Smithy shape ``com.amazonaws.datazone#DataAssetActivityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DataAssetActivityStatus: TypeAlias = Literal[
    "FAILED",
    "PUBLISHING_FAILED",
    "SUCCEEDED_CREATED",
    "SUCCEEDED_UPDATED",
    "SKIPPED_ALREADY_IMPORTED",
    "SKIPPED_ARCHIVED",
    "SKIPPED_NO_ACCESS",
    "UNCHANGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "PUBLISHING_FAILED",
        "SUCCEEDED_CREATED",
        "SUCCEEDED_UPDATED",
        "SKIPPED_ALREADY_IMPORTED",
        "SKIPPED_ARCHIVED",
        "SKIPPED_NO_ACCESS",
        "UNCHANGED",
    )
)


def serialize_json(value: DataAssetActivityStatus) -> str:
    return value


def deserialize_json(data: str) -> DataAssetActivityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataAssetActivityStatus value: {data!r}")
    return cast(DataAssetActivityStatus, data)
