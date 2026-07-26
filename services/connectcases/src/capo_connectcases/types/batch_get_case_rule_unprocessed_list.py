"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetCaseRuleUnprocessedList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_id

BatchGetCaseRuleUnprocessedList: TypeAlias = list[
    "capo_connectcases.types.case_rule_id.CaseRuleId"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetCaseRuleUnprocessedList) -> list:
    return list(value)


def deserialize_json(data: list) -> BatchGetCaseRuleUnprocessedList:
    return list(data)
