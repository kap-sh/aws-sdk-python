"""Generated from Smithy shape ``com.amazonaws.connect#ViewSearchSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.view

ViewSearchSummaryList: TypeAlias = list["capo_connect.types.view.View"]


# --- restJson1 ser/de ---
def serialize_json(value: ViewSearchSummaryList) -> list:
    import capo_connect.types.view

    out: list = []
    for item in value:
        out.append(capo_connect.types.view.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViewSearchSummaryList:
    import capo_connect.types.view

    out: ViewSearchSummaryList = []
    for item in data:
        out.append(capo_connect.types.view.deserialize_json(item))
    return out
