"""Generated from Smithy shape ``com.amazonaws.outposts#LineItemRequestListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.line_item_request

LineItemRequestListDefinition: TypeAlias = list[
    "capo_outposts.types.line_item_request.LineItemRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemRequestListDefinition) -> list:
    import capo_outposts.types.line_item_request

    out: list = []
    for item in value:
        out.append(capo_outposts.types.line_item_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineItemRequestListDefinition:
    import capo_outposts.types.line_item_request

    out: LineItemRequestListDefinition = []
    for item in data:
        out.append(capo_outposts.types.line_item_request.deserialize_json(item))
    return out
