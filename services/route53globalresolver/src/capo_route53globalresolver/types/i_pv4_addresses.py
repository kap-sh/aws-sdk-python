"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#IPv4Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.i_pv4_address

IPv4Addresses: TypeAlias = list[
    "capo_route53globalresolver.types.i_pv4_address.IPv4Address"
]


# --- restJson1 ser/de ---
def serialize_json(value: IPv4Addresses) -> list:
    return list(value)


def deserialize_json(data: list) -> IPv4Addresses:
    return list(data)
