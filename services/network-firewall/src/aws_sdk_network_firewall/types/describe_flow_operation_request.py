"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFlowOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.availability_zone
    import aws_sdk_network_firewall.types.flow_operation_id
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.vpc_endpoint_id


class DescribeFlowOperationRequest(TypedDict, closed=True):
    firewall_arn: "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_network_firewall.types.availability_zone.AvailabilityZone"
    ]
    """<p>The ID of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>"""
    vpc_endpoint_association_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>"""
    vpc_endpoint_id: NotRequired[
        "aws_sdk_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>A unique identifier for the primary endpoint associated with a firewall.</p>"""
    flow_operation_id: (
        "aws_sdk_network_firewall.types.flow_operation_id.FlowOperationId"
    )
    """<p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFlowOperationRequest) -> dict:
    out: dict = {}
    out["FirewallArn"] = value["firewall_arn"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "vpc_endpoint_association_arn" in value:
        out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    out["FlowOperationId"] = value["flow_operation_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFlowOperationRequest:
    out: DescribeFlowOperationRequest = {}  # type: ignore[typeddict-item]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    else:
        raise DeserializationError("DescribeFlowOperationRequest.firewall_arn required")
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "VpcEndpointAssociationArn" in data:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if "FlowOperationId" in data:
        out["flow_operation_id"] = data["FlowOperationId"]
    else:
        raise DeserializationError(
            "DescribeFlowOperationRequest.flow_operation_id required"
        )
    return out
