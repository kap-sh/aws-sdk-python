"""Generated from Smithy shape ``com.amazonaws.sesv2#BlacklistReport``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.blacklist_entries
    import capo_sesv2.types.blacklist_item_name

BlacklistReport: TypeAlias = dict[
    "capo_sesv2.types.blacklist_item_name.BlacklistItemName",
    "capo_sesv2.types.blacklist_entries.BlacklistEntries",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: BlacklistReport) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sesv2.types.blacklist_entries

        out[key] = capo_sesv2.types.blacklist_entries.serialize_json(value)
    return out


def deserialize_json(data: dict) -> BlacklistReport:
    out: BlacklistReport = {}
    for key, value in data.items():
        import capo_sesv2.types.blacklist_entries

        out[key] = capo_sesv2.types.blacklist_entries.deserialize_json(value)
    return out
