"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobRefreshSchedulePropertyToOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleExportJobRefreshSchedulePropertyToOverride: TypeAlias = Literal[
    "StartAfterDateTime",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("StartAfterDateTime",))


def serialize_json(value: AssetBundleExportJobRefreshSchedulePropertyToOverride) -> str:
    return value


def deserialize_json(
    data: str,
) -> AssetBundleExportJobRefreshSchedulePropertyToOverride:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleExportJobRefreshSchedulePropertyToOverride value: {data!r}"
        )
    return cast(AssetBundleExportJobRefreshSchedulePropertyToOverride, data)
