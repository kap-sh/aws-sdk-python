"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.impersonation_rule

ImpersonationRuleList: TypeAlias = list[
    "aws_sdk_workmail.types.impersonation_rule.ImpersonationRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationRuleList) -> list:
    import aws_sdk_workmail.types.impersonation_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workmail.types.impersonation_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImpersonationRuleList:
    import aws_sdk_workmail.types.impersonation_rule

    out: ImpersonationRuleList = []
    for item in data:
        out.append(
            aws_sdk_workmail.types.impersonation_rule.deserialize_aws_json_1_1(item)
        )
    return out
