"""Generated from Smithy shape ``com.amazonaws.licensemanager#EntitlementDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.entitlement_data

EntitlementDataList: TypeAlias = list[
    "capo_license_manager.types.entitlement_data.EntitlementData"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementDataList) -> list:
    import capo_license_manager.types.entitlement_data

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.entitlement_data.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntitlementDataList:
    import capo_license_manager.types.entitlement_data

    out: EntitlementDataList = []
    for item in data:
        out.append(
            capo_license_manager.types.entitlement_data.deserialize_aws_json_1_1(item)
        )
    return out
