"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSourcePropertyToOverride``."""

from typing import Literal, TypeAlias, cast

AssetBundleExportJobDataSourcePropertyToOverride: TypeAlias = Literal[
    "Name",
    "DisableSsl",
    "SecretArn",
    "Username",
    "Password",
    "Domain",
    "WorkGroup",
    "Host",
    "Port",
    "Database",
    "DataSetName",
    "Catalog",
    "InstanceId",
    "ClusterId",
    "ManifestFileLocation",
    "Warehouse",
    "RoleArn",
    "ProductType",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobDataSourcePropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobDataSourcePropertyToOverride:
    return cast(AssetBundleExportJobDataSourcePropertyToOverride, data)
