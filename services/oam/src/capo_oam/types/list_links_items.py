"""Generated from Smithy shape ``com.amazonaws.oam#ListLinksItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_oam.types.list_links_item

ListLinksItems: TypeAlias = list["capo_oam.types.list_links_item.ListLinksItem"]


# --- restJson1 ser/de ---
def serialize_json(value: ListLinksItems) -> list:
    import capo_oam.types.list_links_item

    out: list = []
    for item in value:
        out.append(capo_oam.types.list_links_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListLinksItems:
    import capo_oam.types.list_links_item

    out: ListLinksItems = []
    for item in data:
        out.append(capo_oam.types.list_links_item.deserialize_json(item))
    return out
