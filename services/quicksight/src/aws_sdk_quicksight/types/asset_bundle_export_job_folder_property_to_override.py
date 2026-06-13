"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobFolderPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleExportJobFolderPropertyToOverride: TypeAlias = Literal[
    "Name",
    "ParentFolderArn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "ParentFolderArn",
    )
)


def serialize_json(value: AssetBundleExportJobFolderPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobFolderPropertyToOverride:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleExportJobFolderPropertyToOverride value: {data!r}"
        )
    return cast(AssetBundleExportJobFolderPropertyToOverride, data)
