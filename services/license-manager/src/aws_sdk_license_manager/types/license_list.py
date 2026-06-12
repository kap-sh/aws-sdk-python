"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license

LicenseList: TypeAlias = list["aws_sdk_license_manager.types.license.License"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseList) -> list:
    import aws_sdk_license_manager.types.license

    out: list = []
    for item in value:
        out.append(aws_sdk_license_manager.types.license.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseList:
    import aws_sdk_license_manager.types.license

    out: LicenseList = []
    for item in data:
        out.append(aws_sdk_license_manager.types.license.deserialize_aws_json_1_1(item))
    return out
