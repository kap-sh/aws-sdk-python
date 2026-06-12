"""Generated from Smithy shape ``com.amazonaws.outposts#LineItemListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.line_item

LineItemListDefinition: TypeAlias = list["aws_sdk_outposts.types.line_item.LineItem"]


# --- restJson1 ser/de ---
def serialize_json(value: LineItemListDefinition) -> list:
    import aws_sdk_outposts.types.line_item

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.line_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> LineItemListDefinition:
    import aws_sdk_outposts.types.line_item

    out: LineItemListDefinition = []
    for item in data:
        out.append(aws_sdk_outposts.types.line_item.deserialize_json(item))
    return out
