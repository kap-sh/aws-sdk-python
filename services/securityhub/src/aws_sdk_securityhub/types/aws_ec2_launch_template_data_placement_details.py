"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataPlacementDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataPlacementDetails(TypedDict, closed=True):
    affinity: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The affinity setting for an instance on an EC2 Dedicated Host. </p>"""
    availability_zone: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Availability Zone for the instance. </p>"""
    group_name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the placement group for the instance. </p>"""
    host_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The ID of the Dedicated Host for the instance. </p>"""
    host_resource_group_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the host resource group in which to launch the instances. </p>"""
    partition_number: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p> The number of the partition the instance should launch in. </p>"""
    spread_domain: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> Reserved for future use. </p>"""
    tenancy: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of dedicated runs on single-tenant hardware. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2LaunchTemplateDataPlacementDetails) -> dict:
    out: dict = {}
    if "affinity" in value:
        out["Affinity"] = value["affinity"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "host_id" in value:
        out["HostId"] = value["host_id"]
    if "host_resource_group_arn" in value:
        out["HostResourceGroupArn"] = value["host_resource_group_arn"]
    if "partition_number" in value:
        out["PartitionNumber"] = value["partition_number"]
    if "spread_domain" in value:
        out["SpreadDomain"] = value["spread_domain"]
    if "tenancy" in value:
        out["Tenancy"] = value["tenancy"]
    return out


def deserialize_json(data: dict) -> AwsEc2LaunchTemplateDataPlacementDetails:
    out: AwsEc2LaunchTemplateDataPlacementDetails = {}  # type: ignore[typeddict-item]
    if "Affinity" in data:
        out["affinity"] = data["Affinity"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "HostId" in data:
        out["host_id"] = data["HostId"]
    if "HostResourceGroupArn" in data:
        out["host_resource_group_arn"] = data["HostResourceGroupArn"]
    if "PartitionNumber" in data:
        out["partition_number"] = data["PartitionNumber"]
    if "SpreadDomain" in data:
        out["spread_domain"] = data["SpreadDomain"]
    if "Tenancy" in data:
        out["tenancy"] = data["Tenancy"]
    return out
