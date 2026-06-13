"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSetPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleExportJobDataSetPropertyToOverride: TypeAlias = Literal[
    "Name",
    "RefreshFailureEmailAlertStatus",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "RefreshFailureEmailAlertStatus",
    )
)


def serialize_json(value: AssetBundleExportJobDataSetPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobDataSetPropertyToOverride:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleExportJobDataSetPropertyToOverride value: {data!r}"
        )
    return cast(AssetBundleExportJobDataSetPropertyToOverride, data)
