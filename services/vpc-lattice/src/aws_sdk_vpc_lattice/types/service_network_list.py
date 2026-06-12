"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceNetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_summary

ServiceNetworkList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.service_network_summary.ServiceNetworkSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNetworkList) -> list:
    import aws_sdk_vpc_lattice.types.service_network_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_vpc_lattice.types.service_network_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ServiceNetworkList:
    import aws_sdk_vpc_lattice.types.service_network_summary

    out: ServiceNetworkList = []
    for item in data:
        out.append(
            aws_sdk_vpc_lattice.types.service_network_summary.deserialize_json(item)
        )
    return out
