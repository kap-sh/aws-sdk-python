"""Generated from Smithy shape ``com.amazonaws.licensemanager#PrincipalArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn

PrincipalArnList: TypeAlias = list["aws_sdk_license_manager.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrincipalArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PrincipalArnList:
    return list(data)
