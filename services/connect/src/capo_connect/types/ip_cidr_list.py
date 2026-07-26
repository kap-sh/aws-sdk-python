"""Generated from Smithy shape ``com.amazonaws.connect#IpCidrList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.ip_cidr

IpCidrList: TypeAlias = list["capo_connect.types.ip_cidr.IpCidr"]


# --- restJson1 ser/de ---
def serialize_json(value: IpCidrList) -> list:
    return list(value)


def deserialize_json(data: list) -> IpCidrList:
    return list(data)
