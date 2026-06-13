"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleExportFormat: TypeAlias = Literal[
    "CLOUDFORMATION_JSON",
    "QUICKSIGHT_JSON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUDFORMATION_JSON",
        "QUICKSIGHT_JSON",
    )
)


def serialize_json(value: AssetBundleExportFormat) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetBundleExportFormat value: {data!r}")
    return cast(AssetBundleExportFormat, data)
