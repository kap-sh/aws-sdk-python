"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleExportJobStatus: TypeAlias = Literal[
    "QUEUED_FOR_IMMEDIATE_EXECUTION",
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED_FOR_IMMEDIATE_EXECUTION",
        "IN_PROGRESS",
        "SUCCESSFUL",
        "FAILED",
    )
)


def serialize_json(value: AssetBundleExportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleExportJobStatus value: {data!r}"
        )
    return cast(AssetBundleExportJobStatus, data)
