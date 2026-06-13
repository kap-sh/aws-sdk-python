"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobAnalysisPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleExportJobAnalysisPropertyToOverride: TypeAlias = Literal["Name",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Name",))


def serialize_json(value: AssetBundleExportJobAnalysisPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobAnalysisPropertyToOverride:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleExportJobAnalysisPropertyToOverride value: {data!r}"
        )
    return cast(AssetBundleExportJobAnalysisPropertyToOverride, data)
