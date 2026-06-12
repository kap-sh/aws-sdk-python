"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceNetworkVpcAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_summary

ServiceNetworkVpcAssociationList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.service_network_vpc_association_summary.ServiceNetworkVpcAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNetworkVpcAssociationList) -> list:
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_vpc_lattice.types.service_network_vpc_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceNetworkVpcAssociationList:
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_summary

    out: ServiceNetworkVpcAssociationList = []
    for item in data:
        out.append(
            aws_sdk_vpc_lattice.types.service_network_vpc_association_summary.deserialize_json(
                item
            )
        )
    return out
