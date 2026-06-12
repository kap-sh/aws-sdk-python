"""Generated from Smithy shape ``com.amazonaws.oam#ListAttachedLinksItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_oam.types.list_attached_links_item

ListAttachedLinksItems: TypeAlias = list[
    "aws_sdk_oam.types.list_attached_links_item.ListAttachedLinksItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAttachedLinksItems) -> list:
    import aws_sdk_oam.types.list_attached_links_item

    out: list = []
    for item in value:
        out.append(aws_sdk_oam.types.list_attached_links_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListAttachedLinksItems:
    import aws_sdk_oam.types.list_attached_links_item

    out: ListAttachedLinksItems = []
    for item in data:
        out.append(aws_sdk_oam.types.list_attached_links_item.deserialize_json(item))
    return out
