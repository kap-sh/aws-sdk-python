"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobVPCConnectionPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

AssetBundleExportJobVPCConnectionPropertyToOverride: TypeAlias = Literal[
    "Name",
    "DnsResolvers",
    "RoleArn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "DnsResolvers",
        "RoleArn",
    )
)


def serialize_json(value: AssetBundleExportJobVPCConnectionPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobVPCConnectionPropertyToOverride:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleExportJobVPCConnectionPropertyToOverride value: {data!r}"
        )
    return cast(AssetBundleExportJobVPCConnectionPropertyToOverride, data)
