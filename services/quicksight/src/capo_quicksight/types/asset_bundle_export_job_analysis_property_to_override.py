"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobAnalysisPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobAnalysisPropertyToOverride: TypeAlias = Literal["Name",]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobAnalysisPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobAnalysisPropertyToOverride:
    return cast(AssetBundleExportJobAnalysisPropertyToOverride, data)
