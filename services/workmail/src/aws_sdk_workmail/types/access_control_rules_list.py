"""Generated from Smithy shape ``com.amazonaws.workmail#AccessControlRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.access_control_rule

AccessControlRulesList: TypeAlias = list[
    "aws_sdk_workmail.types.access_control_rule.AccessControlRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessControlRulesList) -> list:
    import aws_sdk_workmail.types.access_control_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workmail.types.access_control_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccessControlRulesList:
    import aws_sdk_workmail.types.access_control_rule

    out: AccessControlRulesList = []
    for item in data:
        out.append(
            aws_sdk_workmail.types.access_control_rule.deserialize_aws_json_1_1(item)
        )
    return out
