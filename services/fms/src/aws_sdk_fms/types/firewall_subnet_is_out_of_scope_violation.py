"""Generated from Smithy shape ``com.amazonaws.fms#FirewallSubnetIsOutOfScopeViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.resource_id


class FirewallSubnetIsOutOfScopeViolation(TypedDict, closed=True):
    firewall_subnet_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The ID of the firewall subnet that violates the policy scope.</p>"""
    vpc_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The VPC ID of the firewall subnet that violates the policy scope.</p>"""
    subnet_availability_zone: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone of the firewall subnet that violates the policy scope.</p>"""
    subnet_availability_zone_id: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone ID of the firewall subnet that violates the policy scope.</p>"""
    vpc_endpoint_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The VPC endpoint ID of the firewall subnet that violates the policy scope.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallSubnetIsOutOfScopeViolation) -> dict:
    out: dict = {}
    if "firewall_subnet_id" in value:
        out["FirewallSubnetId"] = value["firewall_subnet_id"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "subnet_availability_zone_id" in value:
        out["SubnetAvailabilityZoneId"] = value["subnet_availability_zone_id"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallSubnetIsOutOfScopeViolation:
    out: FirewallSubnetIsOutOfScopeViolation = {}  # type: ignore[typeddict-item]
    if "FirewallSubnetId" in data:
        out["firewall_subnet_id"] = data["FirewallSubnetId"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetAvailabilityZone" in data:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if "SubnetAvailabilityZoneId" in data:
        out["subnet_availability_zone_id"] = data["SubnetAvailabilityZoneId"]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out
