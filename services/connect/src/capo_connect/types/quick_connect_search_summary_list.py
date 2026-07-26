"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.quick_connect

QuickConnectSearchSummaryList: TypeAlias = list[
    "capo_connect.types.quick_connect.QuickConnect"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectSearchSummaryList) -> list:
    import capo_connect.types.quick_connect

    out: list = []
    for item in value:
        out.append(capo_connect.types.quick_connect.serialize_json(item))
    return out


def deserialize_json(data: list) -> QuickConnectSearchSummaryList:
    import capo_connect.types.quick_connect

    out: QuickConnectSearchSummaryList = []
    for item in data:
        out.append(capo_connect.types.quick_connect.deserialize_json(item))
    return out
