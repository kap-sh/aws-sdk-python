"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateVpcEndpointAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.vpc_endpoint_association
    import aws_sdk_network_firewall.types.vpc_endpoint_association_status


class CreateVpcEndpointAssociationResponse(TypedDict, closed=True):
    vpc_endpoint_association: NotRequired[
        "aws_sdk_network_firewall.types.vpc_endpoint_association.VpcEndpointAssociation"
    ]
    """<p>The configuration settings for the VPC endpoint association. These settings include the firewall and the VPC and subnet to use for the firewall endpoint. </p>"""
    vpc_endpoint_association_status: NotRequired[
        "aws_sdk_network_firewall.types.vpc_endpoint_association_status.VpcEndpointAssociationStatus"
    ]
    """<p>Detailed information about the current status of a <a>VpcEndpointAssociation</a>. You can retrieve this by calling <a>DescribeVpcEndpointAssociation</a> and providing the VPC endpoint association ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVpcEndpointAssociationResponse) -> dict:
    out: dict = {}
    if "vpc_endpoint_association" in value:
        import aws_sdk_network_firewall.types.vpc_endpoint_association

        out["VpcEndpointAssociation"] = (
            aws_sdk_network_firewall.types.vpc_endpoint_association.serialize_aws_json_1_0(
                value["vpc_endpoint_association"]
            )
        )
    if "vpc_endpoint_association_status" in value:
        import aws_sdk_network_firewall.types.vpc_endpoint_association_status

        out["VpcEndpointAssociationStatus"] = (
            aws_sdk_network_firewall.types.vpc_endpoint_association_status.serialize_aws_json_1_0(
                value["vpc_endpoint_association_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVpcEndpointAssociationResponse:
    out: CreateVpcEndpointAssociationResponse = {}  # type: ignore[typeddict-item]
    if "VpcEndpointAssociation" in data:
        import aws_sdk_network_firewall.types.vpc_endpoint_association

        out["vpc_endpoint_association"] = (
            aws_sdk_network_firewall.types.vpc_endpoint_association.deserialize_aws_json_1_0(
                data["VpcEndpointAssociation"]
            )
        )
    if "VpcEndpointAssociationStatus" in data:
        import aws_sdk_network_firewall.types.vpc_endpoint_association_status

        out["vpc_endpoint_association_status"] = (
            aws_sdk_network_firewall.types.vpc_endpoint_association_status.deserialize_aws_json_1_0(
                data["VpcEndpointAssociationStatus"]
            )
        )
    return out
