"""Generated from Smithy shape ``com.amazonaws.datazone#ListingSummaryItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.listing_summary_item

ListingSummaryItems: TypeAlias = list[
    "capo_datazone.types.listing_summary_item.ListingSummaryItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummaryItems) -> list:
    import capo_datazone.types.listing_summary_item

    out: list = []
    for item in value:
        out.append(capo_datazone.types.listing_summary_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListingSummaryItems:
    import capo_datazone.types.listing_summary_item

    out: ListingSummaryItems = []
    for item in data:
        out.append(capo_datazone.types.listing_summary_item.deserialize_json(item))
    return out
