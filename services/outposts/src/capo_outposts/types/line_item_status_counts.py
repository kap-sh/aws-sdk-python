"""Generated from Smithy shape ``com.amazonaws.outposts#LineItemStatusCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.line_item_quantity
    import capo_outposts.types.line_item_status

LineItemStatusCounts: TypeAlias = dict[
    "capo_outposts.types.line_item_status.LineItemStatus",
    "capo_outposts.types.line_item_quantity.LineItemQuantity",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: LineItemStatusCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_outposts.types.line_item_status

        out[capo_outposts.types.line_item_status.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> LineItemStatusCounts:
    out: LineItemStatusCounts = {}
    for key, value in data.items():
        import capo_outposts.types.line_item_status

        out[capo_outposts.types.line_item_status.deserialize_json(key)] = value
    return out
