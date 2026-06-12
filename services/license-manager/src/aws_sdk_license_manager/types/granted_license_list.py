"""Generated from Smithy shape ``com.amazonaws.licensemanager#GrantedLicenseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.granted_license

GrantedLicenseList: TypeAlias = list[
    "aws_sdk_license_manager.types.granted_license.GrantedLicense"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantedLicenseList) -> list:
    import aws_sdk_license_manager.types.granted_license

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.granted_license.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> GrantedLicenseList:
    import aws_sdk_license_manager.types.granted_license

    out: GrantedLicenseList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.granted_license.deserialize_aws_json_1_1(item)
        )
    return out
