"""Generated from Smithy shape ``com.amazonaws.pinpointemail#BlacklistItemNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.blacklist_item_name

BlacklistItemNames: TypeAlias = list[
    "capo_pinpoint_email.types.blacklist_item_name.BlacklistItemName"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlacklistItemNames) -> list:
    return list(value)


def deserialize_json(data: list) -> BlacklistItemNames:
    return list(data)
