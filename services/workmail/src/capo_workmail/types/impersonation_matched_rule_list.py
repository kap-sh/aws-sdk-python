"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationMatchedRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_matched_rule

ImpersonationMatchedRuleList: TypeAlias = list[
    "capo_workmail.types.impersonation_matched_rule.ImpersonationMatchedRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationMatchedRuleList) -> list:
    import capo_workmail.types.impersonation_matched_rule

    out: list = []
    for item in value:
        out.append(
            capo_workmail.types.impersonation_matched_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImpersonationMatchedRuleList:
    import capo_workmail.types.impersonation_matched_rule

    out: ImpersonationMatchedRuleList = []
    for item in data:
        out.append(
            capo_workmail.types.impersonation_matched_rule.deserialize_aws_json_1_1(
                item
            )
        )
    return out
