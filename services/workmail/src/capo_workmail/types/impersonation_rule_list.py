"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.impersonation_rule

ImpersonationRuleList: TypeAlias = list[
    "capo_workmail.types.impersonation_rule.ImpersonationRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationRuleList) -> list:
    import capo_workmail.types.impersonation_rule

    out: list = []
    for item in value:
        out.append(capo_workmail.types.impersonation_rule.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImpersonationRuleList:
    import capo_workmail.types.impersonation_rule

    out: ImpersonationRuleList = []
    for item in data:
        out.append(
            capo_workmail.types.impersonation_rule.deserialize_aws_json_1_1(item)
        )
    return out
