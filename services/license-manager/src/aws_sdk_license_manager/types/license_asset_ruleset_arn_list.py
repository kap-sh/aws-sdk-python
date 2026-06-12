"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetRulesetArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn

LicenseAssetRulesetArnList: TypeAlias = list["aws_sdk_license_manager.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetRulesetArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LicenseAssetRulesetArnList:
    return list(data)
