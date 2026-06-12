"""Generated from Smithy shape ``com.amazonaws.fms#InvalidNetworkAclEntriesViolation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.entry_violations
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.resource_id


class InvalidNetworkAclEntriesViolation(TypedDict):
    vpc: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The VPC where the violation was found. </p>"""
    subnet: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The subnet that's associated with the network ACL.</p>"""
    subnet_availability_zone: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone where the network ACL is in use. </p>"""
    current_associated_network_acl: NotRequired[
        "aws_sdk_fms.types.resource_id.ResourceId"
    ]
    """<p>The network ACL containing the entry violations. </p>"""
    entry_violations: NotRequired["aws_sdk_fms.types.entry_violations.EntryViolations"]
    """<p>Detailed information about the entry violations in the network ACL. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidNetworkAclEntriesViolation) -> dict:
    out: dict = {}
    if "vpc" in value:
        out["Vpc"] = value["vpc"]
    if "subnet" in value:
        out["Subnet"] = value["subnet"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "current_associated_network_acl" in value:
        out["CurrentAssociatedNetworkAcl"] = value["current_associated_network_acl"]
    if "entry_violations" in value:
        import aws_sdk_fms.types.entry_violations

        out["EntryViolations"] = (
            aws_sdk_fms.types.entry_violations.serialize_aws_json_1_1(
                value["entry_violations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidNetworkAclEntriesViolation:
    out: InvalidNetworkAclEntriesViolation = {}  # type: ignore[typeddict-item]
    if "Vpc" in data:
        out["vpc"] = data["Vpc"]
    if "Subnet" in data:
        out["subnet"] = data["Subnet"]
    if "SubnetAvailabilityZone" in data:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if "CurrentAssociatedNetworkAcl" in data:
        out["current_associated_network_acl"] = data["CurrentAssociatedNetworkAcl"]
    if "EntryViolations" in data:
        import aws_sdk_fms.types.entry_violations

        out["entry_violations"] = (
            aws_sdk_fms.types.entry_violations.deserialize_aws_json_1_1(
                data["EntryViolations"]
            )
        )
    return out
