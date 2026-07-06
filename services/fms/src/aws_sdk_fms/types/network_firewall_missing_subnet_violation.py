"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallMissingSubnetViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.resource_id
    import aws_sdk_fms.types.target_violation_reason
    import aws_sdk_fms.types.violation_target


class NetworkFirewallMissingSubnetViolation(TypedDict, closed=True):
    violation_target: NotRequired["aws_sdk_fms.types.violation_target.ViolationTarget"]
    """<p>The ID of the Network Firewall or VPC resource that's in violation.</p>"""
    vpc: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the VPC associated with a violating subnet.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone of a violating subnet. </p>"""
    target_violation_reason: NotRequired[
        "aws_sdk_fms.types.target_violation_reason.TargetViolationReason"
    ]
    """<p>The reason the resource has this violation, if one is available. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallMissingSubnetViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "vpc" in value:
        out["VPC"] = value["vpc"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "target_violation_reason" in value:
        out["TargetViolationReason"] = value["target_violation_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkFirewallMissingSubnetViolation:
    out: NetworkFirewallMissingSubnetViolation = {}  # type: ignore[typeddict-item]
    if "ViolationTarget" in data:
        out["violation_target"] = data["ViolationTarget"]
    if "VPC" in data:
        out["vpc"] = data["VPC"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "TargetViolationReason" in data:
        out["target_violation_reason"] = data["TargetViolationReason"]
    return out
