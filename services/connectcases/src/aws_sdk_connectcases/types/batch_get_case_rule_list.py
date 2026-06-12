"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetCaseRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.get_case_rule_response

BatchGetCaseRuleList: TypeAlias = list[
    "aws_sdk_connectcases.types.get_case_rule_response.GetCaseRuleResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCaseRuleList) -> list:
    import aws_sdk_connectcases.types.get_case_rule_response

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connectcases.types.get_case_rule_response.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchGetCaseRuleList:
    import aws_sdk_connectcases.types.get_case_rule_response

    out: BatchGetCaseRuleList = []
    for item in data:
        out.append(
            aws_sdk_connectcases.types.get_case_rule_response.deserialize_json(item)
        )
    return out
