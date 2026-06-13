"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleImportJobStatus: TypeAlias = Literal[
    "QUEUED_FOR_IMMEDIATE_EXECUTION",
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
    "FAILED_ROLLBACK_IN_PROGRESS",
    "FAILED_ROLLBACK_COMPLETED",
    "FAILED_ROLLBACK_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED_FOR_IMMEDIATE_EXECUTION",
        "IN_PROGRESS",
        "SUCCESSFUL",
        "FAILED",
        "FAILED_ROLLBACK_IN_PROGRESS",
        "FAILED_ROLLBACK_COMPLETED",
        "FAILED_ROLLBACK_ERROR",
    )
)


def serialize_json(value: AssetBundleImportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleImportJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleImportJobStatus value: {data!r}"
        )
    return cast(AssetBundleImportJobStatus, data)
