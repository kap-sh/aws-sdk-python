"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.case_rule_identifier

CaseRuleIdentifierList: TypeAlias = list[
    "aws_sdk_connectcases.types.case_rule_identifier.CaseRuleIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleIdentifierList) -> list:
    import aws_sdk_connectcases.types.case_rule_identifier

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.case_rule_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaseRuleIdentifierList:
    import aws_sdk_connectcases.types.case_rule_identifier

    out: CaseRuleIdentifierList = []
    for item in data:
        out.append(
            aws_sdk_connectcases.types.case_rule_identifier.deserialize_json(item)
        )
    return out
