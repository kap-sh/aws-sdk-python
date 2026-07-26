"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#IPv6Addresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.i_pv6_address

IPv6Addresses: TypeAlias = list[
    "capo_route53globalresolver.types.i_pv6_address.IPv6Address"
]


# --- restJson1 ser/de ---
def serialize_json(value: IPv6Addresses) -> list:
    return list(value)


def deserialize_json(data: list) -> IPv6Addresses:
    return list(data)
