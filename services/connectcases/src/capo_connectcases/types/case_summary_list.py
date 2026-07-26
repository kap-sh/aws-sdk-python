"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.case_summary

CaseSummaryList: TypeAlias = list["capo_connectcases.types.case_summary.CaseSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: CaseSummaryList) -> list:
    import capo_connectcases.types.case_summary

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.case_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaseSummaryList:
    import capo_connectcases.types.case_summary

    out: CaseSummaryList = []
    for item in data:
        out.append(capo_connectcases.types.case_summary.deserialize_json(item))
    return out
