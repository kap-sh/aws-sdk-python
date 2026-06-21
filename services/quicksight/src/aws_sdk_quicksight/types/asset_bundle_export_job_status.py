"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobStatus``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobStatus: TypeAlias = Literal[
    "QUEUED_FOR_IMMEDIATE_EXECUTION",
    "IN_PROGRESS",
    "SUCCESSFUL",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobStatus) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobStatus:
    return cast(AssetBundleExportJobStatus, data)
