"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_identifier

CaseRuleIdentifierList: TypeAlias = list[
    "capo_connectcases.types.case_rule_identifier.CaseRuleIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleIdentifierList) -> list:
    import capo_connectcases.types.case_rule_identifier

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.case_rule_identifier.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaseRuleIdentifierList:
    import capo_connectcases.types.case_rule_identifier

    out: CaseRuleIdentifierList = []
    for item in data:
        out.append(capo_connectcases.types.case_rule_identifier.deserialize_json(item))
    return out
