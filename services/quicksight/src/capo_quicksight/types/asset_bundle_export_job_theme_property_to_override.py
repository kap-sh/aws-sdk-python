"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobThemePropertyToOverride``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobThemePropertyToOverride: TypeAlias = Literal["Name",]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobThemePropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobThemePropertyToOverride:
    return cast(AssetBundleExportJobThemePropertyToOverride, data)
