"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceNetworkVpcEndpointAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_network_endpoint_association

ServiceNetworkVpcEndpointAssociationList: TypeAlias = list[
    "capo_vpc_lattice.types.service_network_endpoint_association.ServiceNetworkEndpointAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNetworkVpcEndpointAssociationList) -> list:
    import capo_vpc_lattice.types.service_network_endpoint_association

    out: list = []
    for item in value:
        out.append(
            capo_vpc_lattice.types.service_network_endpoint_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceNetworkVpcEndpointAssociationList:
    import capo_vpc_lattice.types.service_network_endpoint_association

    out: ServiceNetworkVpcEndpointAssociationList = []
    for item in data:
        out.append(
            capo_vpc_lattice.types.service_network_endpoint_association.deserialize_json(
                item
            )
        )
    return out
