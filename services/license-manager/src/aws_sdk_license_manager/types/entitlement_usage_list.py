"""Generated from Smithy shape ``com.amazonaws.licensemanager#EntitlementUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.entitlement_usage

EntitlementUsageList: TypeAlias = list[
    "aws_sdk_license_manager.types.entitlement_usage.EntitlementUsage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementUsageList) -> list:
    import aws_sdk_license_manager.types.entitlement_usage

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.entitlement_usage.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntitlementUsageList:
    import aws_sdk_license_manager.types.entitlement_usage

    out: EntitlementUsageList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.entitlement_usage.deserialize_aws_json_1_1(
                item
            )
        )
    return out
