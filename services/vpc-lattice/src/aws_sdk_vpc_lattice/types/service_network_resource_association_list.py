"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceNetworkResourceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_resource_association_summary

ServiceNetworkResourceAssociationList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.service_network_resource_association_summary.ServiceNetworkResourceAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNetworkResourceAssociationList) -> list:
    import aws_sdk_vpc_lattice.types.service_network_resource_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_vpc_lattice.types.service_network_resource_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceNetworkResourceAssociationList:
    import aws_sdk_vpc_lattice.types.service_network_resource_association_summary

    out: ServiceNetworkResourceAssociationList = []
    for item in data:
        out.append(
            aws_sdk_vpc_lattice.types.service_network_resource_association_summary.deserialize_json(
                item
            )
        )
    return out
