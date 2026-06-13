"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobThemePropertyToOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleExportJobThemePropertyToOverride: TypeAlias = Literal["Name",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Name",))


def serialize_json(value: AssetBundleExportJobThemePropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobThemePropertyToOverride:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleExportJobThemePropertyToOverride value: {data!r}"
        )
    return cast(AssetBundleExportJobThemePropertyToOverride, data)
