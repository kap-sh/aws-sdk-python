"""Generated from Smithy shape ``com.amazonaws.licensemanager#EntitlementDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.entitlement_data

EntitlementDataList: TypeAlias = list[
    "aws_sdk_license_manager.types.entitlement_data.EntitlementData"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementDataList) -> list:
    import aws_sdk_license_manager.types.entitlement_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.entitlement_data.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntitlementDataList:
    import aws_sdk_license_manager.types.entitlement_data

    out: EntitlementDataList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.entitlement_data.deserialize_aws_json_1_1(
                item
            )
        )
    return out
