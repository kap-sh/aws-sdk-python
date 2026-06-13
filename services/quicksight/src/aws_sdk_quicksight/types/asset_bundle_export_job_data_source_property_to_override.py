"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobDataSourcePropertyToOverride``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: AssetBundleExportJobDataSourcePropertyToOverride) -> str:
    return value


def deserialize_json(data: str) -> AssetBundleExportJobDataSourcePropertyToOverride:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssetBundleExportJobDataSourcePropertyToOverride value: {data!r}"
        )
    return cast(AssetBundleExportJobDataSourcePropertyToOverride, data)
