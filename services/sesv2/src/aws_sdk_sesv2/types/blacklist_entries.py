"""Generated from Smithy shape ``com.amazonaws.sesv2#BlacklistEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.blacklist_entry

BlacklistEntries: TypeAlias = list["aws_sdk_sesv2.types.blacklist_entry.BlacklistEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: BlacklistEntries) -> list:
    import aws_sdk_sesv2.types.blacklist_entry

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.blacklist_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> BlacklistEntries:
    import aws_sdk_sesv2.types.blacklist_entry

    out: BlacklistEntries = []
    for item in data:
        out.append(aws_sdk_sesv2.types.blacklist_entry.deserialize_json(item))
    return out
