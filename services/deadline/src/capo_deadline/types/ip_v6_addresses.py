"""Generated from Smithy shape ``com.amazonaws.deadline#IpV6Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.ip_v6_address

IpV6Addresses: TypeAlias = list["capo_deadline.types.ip_v6_address.IpV6Address"]


# --- restJson1 ser/de ---
def serialize_json(value: IpV6Addresses) -> list:
    return list(value)


def deserialize_json(data: list) -> IpV6Addresses:
    return list(data)
