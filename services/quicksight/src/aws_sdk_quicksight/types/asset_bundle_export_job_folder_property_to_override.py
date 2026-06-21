"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobFolderPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobFolderPropertyToOverride: TypeAlias = Literal[
    "Name",
    "ParentFolderArn",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobFolderPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobFolderPropertyToOverride:
    return cast(AssetBundleExportJobFolderPropertyToOverride, data)
