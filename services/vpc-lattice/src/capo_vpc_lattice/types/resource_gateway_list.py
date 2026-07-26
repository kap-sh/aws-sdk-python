"""Generated from Smithy shape ``com.amazonaws.vpclattice#ResourceGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.resource_gateway_summary

ResourceGatewayList: TypeAlias = list[
    "capo_vpc_lattice.types.resource_gateway_summary.ResourceGatewaySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceGatewayList) -> list:
    import capo_vpc_lattice.types.resource_gateway_summary

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.resource_gateway_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceGatewayList:
    import capo_vpc_lattice.types.resource_gateway_summary

    out: ResourceGatewayList = []
    for item in data:
        out.append(
            capo_vpc_lattice.types.resource_gateway_summary.deserialize_json(item)
        )
    return out
