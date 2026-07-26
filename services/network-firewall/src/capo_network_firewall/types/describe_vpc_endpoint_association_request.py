"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeVpcEndpointAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn


class DescribeVpcEndpointAssociationRequest(TypedDict, closed=True):
    vpc_endpoint_association_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeVpcEndpointAssociationRequest) -> dict:
    out: dict = {}
    out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeVpcEndpointAssociationRequest:
    out: DescribeVpcEndpointAssociationRequest = {}  # type: ignore[typeddict-item]
    if "VpcEndpointAssociationArn" in data:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    else:
        raise DeserializationError(
            "DescribeVpcEndpointAssociationRequest.vpc_endpoint_association_arn required"
        )
    return out
