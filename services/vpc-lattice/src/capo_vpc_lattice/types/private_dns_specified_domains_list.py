"""Generated from Smithy shape ``com.amazonaws.vpclattice#PrivateDnsSpecifiedDomainsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.private_dns_specified_domain

PrivateDnsSpecifiedDomainsList: TypeAlias = list[
    "capo_vpc_lattice.types.private_dns_specified_domain.PrivateDnsSpecifiedDomain"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrivateDnsSpecifiedDomainsList) -> list:
    return list(value)


def deserialize_json(data: list) -> PrivateDnsSpecifiedDomainsList:
    return list(data)
