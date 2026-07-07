"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StartFlowFlushRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.age
    import aws_sdk_network_firewall.types.availability_zone
    import aws_sdk_network_firewall.types.flow_filters
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.vpc_endpoint_id


class StartFlowFlushRequest(TypedDict, closed=True):
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
    minimum_flow_age_in_seconds: NotRequired["aws_sdk_network_firewall.types.age.Age"]
    """<p>The reqested <code>FlowOperation</code> ignores flows with an age (in seconds) lower than <code>MinimumFlowAgeInSeconds</code>. You provide this for start commands.</p>"""
    flow_filters: "aws_sdk_network_firewall.types.flow_filters.FlowFilters"
    """<p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFlowFlushRequest) -> dict:
    out: dict = {}
    out["FirewallArn"] = value["firewall_arn"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "vpc_endpoint_association_arn" in value:
        out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "minimum_flow_age_in_seconds" in value:
        out["MinimumFlowAgeInSeconds"] = value["minimum_flow_age_in_seconds"]
    import aws_sdk_network_firewall.types.flow_filters

    out["FlowFilters"] = (
        aws_sdk_network_firewall.types.flow_filters.serialize_aws_json_1_0(
            value["flow_filters"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFlowFlushRequest:
    out: StartFlowFlushRequest = {}  # type: ignore[typeddict-item]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    else:
        raise DeserializationError("StartFlowFlushRequest.firewall_arn required")
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "VpcEndpointAssociationArn" in data:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if "MinimumFlowAgeInSeconds" in data:
        out["minimum_flow_age_in_seconds"] = data["MinimumFlowAgeInSeconds"]
    if "FlowFilters" in data:
        import aws_sdk_network_firewall.types.flow_filters

        out["flow_filters"] = (
            aws_sdk_network_firewall.types.flow_filters.deserialize_aws_json_1_0(
                data["FlowFilters"]
            )
        )
    else:
        raise DeserializationError("StartFlowFlushRequest.flow_filters required")
    return out
