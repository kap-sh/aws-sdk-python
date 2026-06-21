"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobVPCConnectionPropertyToOverride``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobVPCConnectionPropertyToOverride: TypeAlias = Literal[
    "Name",
    "DnsResolvers",
    "RoleArn",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobVPCConnectionPropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobVPCConnectionPropertyToOverride:
    return cast(AssetBundleExportJobVPCConnectionPropertyToOverride, data)
