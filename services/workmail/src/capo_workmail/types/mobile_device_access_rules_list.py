"""Generated from Smithy shape ``com.amazonaws.workmail#MobileDeviceAccessRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.mobile_device_access_rule

MobileDeviceAccessRulesList: TypeAlias = list[
    "capo_workmail.types.mobile_device_access_rule.MobileDeviceAccessRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MobileDeviceAccessRulesList) -> list:
    import capo_workmail.types.mobile_device_access_rule

    out: list = []
    for item in value:
        out.append(
            capo_workmail.types.mobile_device_access_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MobileDeviceAccessRulesList:
    import capo_workmail.types.mobile_device_access_rule

    out: MobileDeviceAccessRulesList = []
    for item in data:
        out.append(
            capo_workmail.types.mobile_device_access_rule.deserialize_aws_json_1_1(item)
        )
    return out
