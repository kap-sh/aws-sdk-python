"""Generated from Smithy shape ``com.amazonaws.vpclattice#ResourceEndpointAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.resource_endpoint_association_summary

ResourceEndpointAssociationList: TypeAlias = list[
    "capo_vpc_lattice.types.resource_endpoint_association_summary.ResourceEndpointAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceEndpointAssociationList) -> list:
    import capo_vpc_lattice.types.resource_endpoint_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_vpc_lattice.types.resource_endpoint_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourceEndpointAssociationList:
    import capo_vpc_lattice.types.resource_endpoint_association_summary

    out: ResourceEndpointAssociationList = []
    for item in data:
        out.append(
            capo_vpc_lattice.types.resource_endpoint_association_summary.deserialize_json(
                item
            )
        )
    return out
