"""Generated from Smithy shape ``com.amazonaws.outposts#LineItemListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.line_item

LineItemListDefinition: TypeAlias = list["capo_outposts.types.line_item.LineItem"]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemListDefinition) -> list:
    import capo_outposts.types.line_item

    out: list = []
    for item in value:
        out.append(capo_outposts.types.line_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineItemListDefinition:
    import capo_outposts.types.line_item

    out: LineItemListDefinition = []
    for item in data:
        out.append(capo_outposts.types.line_item.deserialize_json(item))
    return out
