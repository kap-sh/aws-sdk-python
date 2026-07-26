"""Generated from Smithy shape ``com.amazonaws.billingconductor#LineItemFiltersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.line_item_filter

LineItemFiltersList: TypeAlias = list[
    "capo_billingconductor.types.line_item_filter.LineItemFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemFiltersList) -> list:
    import capo_billingconductor.types.line_item_filter

    out: list = []
    for item in value:
        out.append(capo_billingconductor.types.line_item_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineItemFiltersList:
    import capo_billingconductor.types.line_item_filter

    out: LineItemFiltersList = []
    for item in data:
        out.append(capo_billingconductor.types.line_item_filter.deserialize_json(item))
    return out
