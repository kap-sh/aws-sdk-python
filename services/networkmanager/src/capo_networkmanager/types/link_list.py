"""Generated from Smithy shape ``com.amazonaws.networkmanager#LinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.link

LinkList: TypeAlias = list["capo_networkmanager.types.link.Link"]


# --- restJson1 ser/de ---
def serialize_json(value: LinkList) -> list:
    import capo_networkmanager.types.link

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.link.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinkList:
    import capo_networkmanager.types.link

    out: LinkList = []
    for item in data:
        out.append(capo_networkmanager.types.link.deserialize_json(item))
    return out
