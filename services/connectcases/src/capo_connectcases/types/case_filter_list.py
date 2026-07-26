"""Generated from Smithy shape ``com.amazonaws.connectcases#CaseFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.case_filter

CaseFilterList: TypeAlias = list["capo_connectcases.types.case_filter.CaseFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: CaseFilterList) -> list:
    import capo_connectcases.types.case_filter

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.case_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CaseFilterList:
    import capo_connectcases.types.case_filter

    out: CaseFilterList = []
    for item in data:
        out.append(capo_connectcases.types.case_filter.deserialize_json(item))
    return out
