"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VpcEndpointAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.vpc_endpoint_association_metadata

VpcEndpointAssociations: TypeAlias = list[
    "aws_sdk_network_firewall.types.vpc_endpoint_association_metadata.VpcEndpointAssociationMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointAssociations) -> list:
    import aws_sdk_network_firewall.types.vpc_endpoint_association_metadata

    out: list = []
    for item in value:
        out.append(
            aws_sdk_network_firewall.types.vpc_endpoint_association_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VpcEndpointAssociations:
    import aws_sdk_network_firewall.types.vpc_endpoint_association_metadata

    out: VpcEndpointAssociations = []
    for item in data:
        out.append(
            aws_sdk_network_firewall.types.vpc_endpoint_association_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
