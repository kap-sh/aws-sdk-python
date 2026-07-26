"""Generated from Smithy shape ``com.amazonaws.appstream#AdminAppLicenseUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.admin_app_license_usage_record

AdminAppLicenseUsageList: TypeAlias = list[
    "capo_appstream.types.admin_app_license_usage_record.AdminAppLicenseUsageRecord"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminAppLicenseUsageList) -> list:
    import capo_appstream.types.admin_app_license_usage_record

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.admin_app_license_usage_record.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdminAppLicenseUsageList:
    import capo_appstream.types.admin_app_license_usage_record

    out: AdminAppLicenseUsageList = []
    for item in data:
        out.append(
            capo_appstream.types.admin_app_license_usage_record.deserialize_aws_json_1_1(
                item
            )
        )
    return out
