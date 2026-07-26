"""Generated from Smithy shape ``com.amazonaws.connect#NextContacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.next_contact_entry

NextContacts: TypeAlias = list["capo_connect.types.next_contact_entry.NextContactEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: NextContacts) -> list:
    import capo_connect.types.next_contact_entry

    out: list = []
    for item in value:
        out.append(capo_connect.types.next_contact_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> NextContacts:
    import capo_connect.types.next_contact_entry

    out: NextContacts = []
    for item in data:
        out.append(capo_connect.types.next_contact_entry.deserialize_json(item))
    return out
