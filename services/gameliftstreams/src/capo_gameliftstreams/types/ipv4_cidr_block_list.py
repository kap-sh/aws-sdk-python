"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#Ipv4CidrBlockList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gameliftstreams.types.ipv4_cidr_block

Ipv4CidrBlockList: TypeAlias = list[
    "capo_gameliftstreams.types.ipv4_cidr_block.Ipv4CidrBlock"
]


# --- restJson1 ser/de ---
def serialize_json(value: Ipv4CidrBlockList) -> list:
    return list(value)


def deserialize_json(data: list) -> Ipv4CidrBlockList:
    return list(data)
