"""Generated from Smithy shape ``com.amazonaws.oam#ListLinksItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_oam.types.list_links_item

ListLinksItems: TypeAlias = list["aws_sdk_oam.types.list_links_item.ListLinksItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ListLinksItems) -> list:
    import aws_sdk_oam.types.list_links_item

    out: list = []
    for item in value:
        out.append(aws_sdk_oam.types.list_links_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListLinksItems:
    import aws_sdk_oam.types.list_links_item

    out: ListLinksItems = []
    for item in data:
        out.append(aws_sdk_oam.types.list_links_item.deserialize_json(item))
    return out
