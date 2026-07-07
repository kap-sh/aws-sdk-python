"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListFlowOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.availability_zone
    import aws_sdk_network_firewall.types.flow_operation_type
    import aws_sdk_network_firewall.types.pagination_max_results
    import aws_sdk_network_firewall.types.pagination_token
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.vpc_endpoint_id


class ListFlowOperationsRequest(TypedDict, closed=True):
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
    flow_operation_type: NotRequired[
        "aws_sdk_network_firewall.types.flow_operation_type.FlowOperationType"
    ]
    """<p>An optional string that defines whether any or all operation types are returned.</p>"""
    next_token: NotRequired[
        "aws_sdk_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    max_results: NotRequired[
        "aws_sdk_network_firewall.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFlowOperationsRequest) -> dict:
    out: dict = {}
    out["FirewallArn"] = value["firewall_arn"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "vpc_endpoint_association_arn" in value:
        out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "flow_operation_type" in value:
        import aws_sdk_network_firewall.types.flow_operation_type

        out["FlowOperationType"] = (
            aws_sdk_network_firewall.types.flow_operation_type.serialize_aws_json_1_0(
                value["flow_operation_type"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFlowOperationsRequest:
    out: ListFlowOperationsRequest = {}  # type: ignore[typeddict-item]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    else:
        raise DeserializationError("ListFlowOperationsRequest.firewall_arn required")
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "VpcEndpointAssociationArn" in data:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if "FlowOperationType" in data:
        import aws_sdk_network_firewall.types.flow_operation_type

        out["flow_operation_type"] = (
            aws_sdk_network_firewall.types.flow_operation_type.deserialize_aws_json_1_0(
                data["FlowOperationType"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
