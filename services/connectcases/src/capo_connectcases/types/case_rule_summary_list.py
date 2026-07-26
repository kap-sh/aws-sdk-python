"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseRuleSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.case_rule_summary

CaseRuleSummaryList: TypeAlias = list[
    "capo_connectcases.types.case_rule_summary.CaseRuleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CaseRuleSummaryList) -> list:
    import capo_connectcases.types.case_rule_summary

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.case_rule_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaseRuleSummaryList:
    import capo_connectcases.types.case_rule_summary

    out: CaseRuleSummaryList = []
    for item in data:
        out.append(capo_connectcases.types.case_rule_summary.deserialize_json(item))
    return out
