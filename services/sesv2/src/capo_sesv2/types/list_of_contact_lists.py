"""Generated from Smithy shape ``com.amazonaws.sesv2#ListOfContactLists``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.contact_list

ListOfContactLists: TypeAlias = list["capo_sesv2.types.contact_list.ContactList"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfContactLists) -> list:
    import capo_sesv2.types.contact_list

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.contact_list.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfContactLists:
    import capo_sesv2.types.contact_list

    out: ListOfContactLists = []
    for item in data:
        out.append(capo_sesv2.types.contact_list.deserialize_json(item))
    return out
