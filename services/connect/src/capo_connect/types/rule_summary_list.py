"""Generated from Smithy shape ``com.amazonaws.connect#RuleSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.rule_summary

RuleSummaryList: TypeAlias = list["capo_connect.types.rule_summary.RuleSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummaryList) -> list:
    import capo_connect.types.rule_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.rule_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleSummaryList:
    import capo_connect.types.rule_summary

    out: RuleSummaryList = []
    for item in data:
        out.append(capo_connect.types.rule_summary.deserialize_json(item))
    return out
