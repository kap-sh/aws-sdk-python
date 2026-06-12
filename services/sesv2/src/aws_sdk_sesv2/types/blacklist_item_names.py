"""Generated from Smithy shape ``com.amazonaws.sesv2#BlacklistItemNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.blacklist_item_name

BlacklistItemNames: TypeAlias = list[
    "aws_sdk_sesv2.types.blacklist_item_name.BlacklistItemName"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlacklistItemNames) -> list:
    return list(value)


def deserialize_json(data: list) -> BlacklistItemNames:
    return list(data)
