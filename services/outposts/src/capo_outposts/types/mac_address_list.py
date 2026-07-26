"""Generated from Smithy shape ``com.amazonaws.outposts#MacAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.mac_address

MacAddressList: TypeAlias = list["capo_outposts.types.mac_address.MacAddress"]


# --- restJson1 ser/de ---
def serialize_json(value: MacAddressList) -> list:
    return list(value)


def deserialize_json(data: list) -> MacAddressList:
    return list(data)
