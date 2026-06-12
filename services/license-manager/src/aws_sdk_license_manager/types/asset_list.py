"""Generated from Smithy shape ``com.amazonaws.licensemanager#AssetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.asset

AssetList: TypeAlias = list["aws_sdk_license_manager.types.asset.Asset"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetList) -> list:
    import aws_sdk_license_manager.types.asset

    out: list = []
    for item in value:
        out.append(aws_sdk_license_manager.types.asset.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AssetList:
    import aws_sdk_license_manager.types.asset

    out: AssetList = []
    for item in data:
        out.append(aws_sdk_license_manager.types.asset.deserialize_aws_json_1_1(item))
    return out
