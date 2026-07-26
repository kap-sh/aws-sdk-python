"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.field_summary

FieldSummaryList: TypeAlias = list["capo_connectcases.types.field_summary.FieldSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldSummaryList) -> list:
    import capo_connectcases.types.field_summary

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.field_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldSummaryList:
    import capo_connectcases.types.field_summary

    out: FieldSummaryList = []
    for item in data:
        out.append(capo_connectcases.types.field_summary.deserialize_json(item))
    return out
