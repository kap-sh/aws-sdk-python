"""Generated from Smithy shape ``com.amazonaws.deadline#IpV4Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.ip_v4_address

IpV4Addresses: TypeAlias = list["capo_deadline.types.ip_v4_address.IpV4Address"]


# --- restJson1 ser/de ---
def serialize_json(value: IpV4Addresses) -> list:
    return list(value)


def deserialize_json(data: list) -> IpV4Addresses:
    return list(data)
