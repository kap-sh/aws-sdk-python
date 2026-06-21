"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSetPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobDataSetPropertyToOverride: TypeAlias = Literal[
    "Name",
    "RefreshFailureEmailAlertStatus",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDataSetPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobDataSetPropertyToOverride:
    return cast(AssetBundleExportJobDataSetPropertyToOverride, data)
