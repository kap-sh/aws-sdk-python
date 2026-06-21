"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobRefreshSchedulePropertyToOverride``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobRefreshSchedulePropertyToOverride: TypeAlias = Literal[
    "StartAfterDateTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobRefreshSchedulePropertyToOverride) -> str:
    return value


def deserialize_json(
    data: str,
) -> AssetBundleExportJobRefreshSchedulePropertyToOverride:
    return cast(AssetBundleExportJobRefreshSchedulePropertyToOverride, data)
