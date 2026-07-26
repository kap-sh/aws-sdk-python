"""Generated from Smithy shape ``com.amazonaws.connectcases#LayoutSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.layout_summary

LayoutSummaryList: TypeAlias = list[
    "capo_connectcases.types.layout_summary.LayoutSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LayoutSummaryList) -> list:
    import capo_connectcases.types.layout_summary

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.layout_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayoutSummaryList:
    import capo_connectcases.types.layout_summary

    out: LayoutSummaryList = []
    for item in data:
        out.append(capo_connectcases.types.layout_summary.deserialize_json(item))
    return out
