"""Generated from Smithy shape ``com.amazonaws.sesv2#BlacklistEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.blacklist_entry

BlacklistEntries: TypeAlias = list["capo_sesv2.types.blacklist_entry.BlacklistEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: BlacklistEntries) -> list:
    import capo_sesv2.types.blacklist_entry

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.blacklist_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> BlacklistEntries:
    import capo_sesv2.types.blacklist_entry

    out: BlacklistEntries = []
    for item in data:
        out.append(capo_sesv2.types.blacklist_entry.deserialize_json(item))
    return out
