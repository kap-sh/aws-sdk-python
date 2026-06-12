"""Generated from Smithy shape ``com.amazonaws.appstream#AdminAppLicenseUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.admin_app_license_usage_record

AdminAppLicenseUsageList: TypeAlias = list[
    "aws_sdk_appstream.types.admin_app_license_usage_record.AdminAppLicenseUsageRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminAppLicenseUsageList) -> list:
    import aws_sdk_appstream.types.admin_app_license_usage_record

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appstream.types.admin_app_license_usage_record.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdminAppLicenseUsageList:
    import aws_sdk_appstream.types.admin_app_license_usage_record

    out: AdminAppLicenseUsageList = []
    for item in data:
        out.append(
            aws_sdk_appstream.types.admin_app_license_usage_record.deserialize_aws_json_1_1(
                item
            )
        )
    return out
