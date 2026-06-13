"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDashboardPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleExportJobDashboardPropertyToOverride: TypeAlias = Literal["Name",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Name",))


def serialize_json(value: AssetBundleExportJobDashboardPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobDashboardPropertyToOverride:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleExportJobDashboardPropertyToOverride value: {data!r}"
        )
    return cast(AssetBundleExportJobDashboardPropertyToOverride, data)
