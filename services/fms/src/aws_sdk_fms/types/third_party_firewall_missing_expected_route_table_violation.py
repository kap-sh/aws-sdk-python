"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewallMissingExpectedRouteTableViolation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.resource_id
    import aws_sdk_fms.types.violation_target


class ThirdPartyFirewallMissingExpectedRouteTableViolation(TypedDict):
    violation_target: NotRequired["aws_sdk_fms.types.violation_target.ViolationTarget"]
    """<p>The ID of the third-party firewall or VPC resource that's causing the violation.</p>"""
    vpc: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the VPC associated with a fireawll subnet that's causing the violation.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone of the firewall subnet that's causing the violation.</p>"""
    current_route_table: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the current route table that's associated with the subnet, if one is available.</p>"""
    expected_route_table: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the route table that should be associated with the subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ThirdPartyFirewallMissingExpectedRouteTableViolation,
) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "vpc" in value:
        out["VPC"] = value["vpc"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "current_route_table" in value:
        out["CurrentRouteTable"] = value["current_route_table"]
    if "expected_route_table" in value:
        out["ExpectedRouteTable"] = value["expected_route_table"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ThirdPartyFirewallMissingExpectedRouteTableViolation:
    out: ThirdPartyFirewallMissingExpectedRouteTableViolation = {}  # type: ignore[typeddict-item]
    if "ViolationTarget" in data:
        out["violation_target"] = data["ViolationTarget"]
    if "VPC" in data:
        out["vpc"] = data["VPC"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "CurrentRouteTable" in data:
        out["current_route_table"] = data["CurrentRouteTable"]
    if "ExpectedRouteTable" in data:
        out["expected_route_table"] = data["ExpectedRouteTable"]
    return out
