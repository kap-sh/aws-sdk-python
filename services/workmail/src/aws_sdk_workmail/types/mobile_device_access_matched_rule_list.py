"""Generated from Smithy shape ``com.amazonaws.workmail#MobileDeviceAccessMatchedRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.mobile_device_access_matched_rule

MobileDeviceAccessMatchedRuleList: TypeAlias = list[
    "aws_sdk_workmail.types.mobile_device_access_matched_rule.MobileDeviceAccessMatchedRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MobileDeviceAccessMatchedRuleList) -> list:
    import aws_sdk_workmail.types.mobile_device_access_matched_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workmail.types.mobile_device_access_matched_rule.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MobileDeviceAccessMatchedRuleList:
    import aws_sdk_workmail.types.mobile_device_access_matched_rule

    out: MobileDeviceAccessMatchedRuleList = []
    for item in data:
        out.append(
            aws_sdk_workmail.types.mobile_device_access_matched_rule.deserialize_aws_json_1_1(
                item
            )
        )
    return out
