"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: AssetBundleImportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleImportJobStatus:
    return cast(AssetBundleImportJobStatus, data)
