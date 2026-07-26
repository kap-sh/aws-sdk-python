"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetCaseRuleErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_error

BatchGetCaseRuleErrorList: TypeAlias = list[
    "capo_connectcases.types.case_rule_error.CaseRuleError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCaseRuleErrorList) -> list:
    import capo_connectcases.types.case_rule_error

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.case_rule_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetCaseRuleErrorList:
    import capo_connectcases.types.case_rule_error

    out: BatchGetCaseRuleErrorList = []
    for item in data:
        out.append(capo_connectcases.types.case_rule_error.deserialize_json(item))
    return out
