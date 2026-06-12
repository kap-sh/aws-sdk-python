"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceNetworkServiceAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.service_network_service_association_summary

ServiceNetworkServiceAssociationList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.service_network_service_association_summary.ServiceNetworkServiceAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNetworkServiceAssociationList) -> list:
    import aws_sdk_vpc_lattice.types.service_network_service_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_vpc_lattice.types.service_network_service_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ServiceNetworkServiceAssociationList:
    import aws_sdk_vpc_lattice.types.service_network_service_association_summary

    out: ServiceNetworkServiceAssociationList = []
    for item in data:
        out.append(
            aws_sdk_vpc_lattice.types.service_network_service_association_summary.deserialize_json(
                item
            )
        )
    return out
