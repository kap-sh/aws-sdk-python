"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceNetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_network_summary

ServiceNetworkList: TypeAlias = list[
    "capo_vpc_lattice.types.service_network_summary.ServiceNetworkSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNetworkList) -> list:
    import capo_vpc_lattice.types.service_network_summary

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.service_network_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceNetworkList:
    import capo_vpc_lattice.types.service_network_summary

    out: ServiceNetworkList = []
    for item in data:
        out.append(
            capo_vpc_lattice.types.service_network_summary.deserialize_json(item)
        )
    return out
