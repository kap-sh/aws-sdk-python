"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportFormat``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportFormat: TypeAlias = Literal[
    "CLOUDFORMATION_JSON",
    "QUICKSIGHT_JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportFormat) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportFormat:
    return cast(AssetBundleExportFormat, data)
