"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.quick_connect_summary

QuickConnectSummaryList: TypeAlias = list[
    "capo_connect.types.quick_connect_summary.QuickConnectSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectSummaryList) -> list:
    import capo_connect.types.quick_connect_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.quick_connect_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuickConnectSummaryList:
    import capo_connect.types.quick_connect_summary

    out: QuickConnectSummaryList = []
    for item in data:
        out.append(capo_connect.types.quick_connect_summary.deserialize_json(item))
    return out
