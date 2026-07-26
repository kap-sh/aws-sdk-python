"""Generated from Smithy shape ``com.amazonaws.billingconductor#LineItemFilterValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.line_item_filter_value

LineItemFilterValuesList: TypeAlias = list[
    "capo_billingconductor.types.line_item_filter_value.LineItemFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemFilterValuesList) -> list:
    import capo_billingconductor.types.line_item_filter_value

    out: list = []
    for item in value:
        out.append(
            capo_billingconductor.types.line_item_filter_value.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LineItemFilterValuesList:
    import capo_billingconductor.types.line_item_filter_value

    out: LineItemFilterValuesList = []
    for item in data:
        out.append(
            capo_billingconductor.types.line_item_filter_value.deserialize_json(item)
        )
    return out
