"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDashboardPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobDashboardPropertyToOverride: TypeAlias = Literal["Name",]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDashboardPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobDashboardPropertyToOverride:
    return cast(AssetBundleExportJobDashboardPropertyToOverride, data)
