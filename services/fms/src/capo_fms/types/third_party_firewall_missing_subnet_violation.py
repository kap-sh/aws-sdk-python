"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewallMissingSubnetViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_id
    import capo_fms.types.target_violation_reason
    import capo_fms.types.violation_target


class ThirdPartyFirewallMissingSubnetViolation(TypedDict, closed=True):
    violation_target: NotRequired["capo_fms.types.violation_target.ViolationTarget"]
    """<p>The ID of the third-party firewall or VPC resource that's causing the violation.</p>"""
    vpc: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the VPC associated with a subnet that's causing the violation.</p>"""
    availability_zone: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone of a subnet that's causing the violation.</p>"""
    target_violation_reason: NotRequired[
        "capo_fms.types.target_violation_reason.TargetViolationReason"
    ]
    """<p>The reason the resource is causing the violation, if a reason is available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyFirewallMissingSubnetViolation) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ThirdPartyFirewallMissingSubnetViolation:
    out: ThirdPartyFirewallMissingSubnetViolation = {}  # type: ignore[typeddict-item]
    if "ViolationTarget" in data:
        out["violation_target"] = data["ViolationTarget"]
    if "VPC" in data:
        out["vpc"] = data["VPC"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "TargetViolationReason" in data:
        out["target_violation_reason"] = data["TargetViolationReason"]
    return out
