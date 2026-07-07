"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeFirewallMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.firewall_status_value
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.supported_availability_zones
    import aws_sdk_network_firewall.types.transit_gateway_attachment_id


class DescribeFirewallMetadataResponse(TypedDict, closed=True):
    firewall_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    firewall_policy_arn: NotRequired[
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the firewall policy.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the firewall.</p>"""
    status: NotRequired[
        "aws_sdk_network_firewall.types.firewall_status_value.FirewallStatusValue"
    ]
    """<p>The readiness of the configured firewall to handle network traffic across all of the Availability Zones where you have it configured. This setting is <code>READY</code> only when the <code>ConfigurationSyncStateSummary</code> value is <code>IN_SYNC</code> and the <code>Attachment</code> <code>Status</code> values for all of the configured subnets are <code>READY</code>. </p>"""
    supported_availability_zones: NotRequired[
        "aws_sdk_network_firewall.types.supported_availability_zones.SupportedAvailabilityZones"
    ]
    """<p>The Availability Zones that the firewall currently supports. This includes all Availability Zones for which the firewall has a subnet defined. </p>"""
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_network_firewall.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The unique identifier of the transit gateway attachment associated with this firewall. This field is only present for transit gateway-attached firewalls.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeFirewallMetadataResponse) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_policy_arn" in value:
        out["FirewallPolicyArn"] = value["firewall_policy_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import aws_sdk_network_firewall.types.firewall_status_value

        out["Status"] = (
            aws_sdk_network_firewall.types.firewall_status_value.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "supported_availability_zones" in value:
        import aws_sdk_network_firewall.types.supported_availability_zones

        out["SupportedAvailabilityZones"] = (
            aws_sdk_network_firewall.types.supported_availability_zones.serialize_aws_json_1_0(
                value["supported_availability_zones"]
            )
        )
    if "transit_gateway_attachment_id" in value:
        out["TransitGatewayAttachmentId"] = value["transit_gateway_attachment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeFirewallMetadataResponse:
    out: DescribeFirewallMetadataResponse = {}  # type: ignore[typeddict-item]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    if "FirewallPolicyArn" in data:
        out["firewall_policy_arn"] = data["FirewallPolicyArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_network_firewall.types.firewall_status_value

        out["status"] = (
            aws_sdk_network_firewall.types.firewall_status_value.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "SupportedAvailabilityZones" in data:
        import aws_sdk_network_firewall.types.supported_availability_zones

        out["supported_availability_zones"] = (
            aws_sdk_network_firewall.types.supported_availability_zones.deserialize_aws_json_1_0(
                data["SupportedAvailabilityZones"]
            )
        )
    if "TransitGatewayAttachmentId" in data:
        out["transit_gateway_attachment_id"] = data["TransitGatewayAttachmentId"]
    return out
