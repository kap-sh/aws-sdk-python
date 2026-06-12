"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationMatchedRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.impersonation_matched_rule

ImpersonationMatchedRuleList: TypeAlias = list[
    "aws_sdk_workmail.types.impersonation_matched_rule.ImpersonationMatchedRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationMatchedRuleList) -> list:
    import aws_sdk_workmail.types.impersonation_matched_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workmail.types.impersonation_matched_rule.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImpersonationMatchedRuleList:
    import aws_sdk_workmail.types.impersonation_matched_rule

    out: ImpersonationMatchedRuleList = []
    for item in data:
        out.append(
            aws_sdk_workmail.types.impersonation_matched_rule.deserialize_aws_json_1_1(
                item
            )
        )
    return out
