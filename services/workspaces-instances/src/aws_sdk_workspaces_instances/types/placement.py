"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Placement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.arn
    import aws_sdk_workspaces_instances.types.availability_zone
    import aws_sdk_workspaces_instances.types.host_id
    import aws_sdk_workspaces_instances.types.non_negative_integer
    import aws_sdk_workspaces_instances.types.placement_group_id
    import aws_sdk_workspaces_instances.types.string64
    import aws_sdk_workspaces_instances.types.tenancy_enum


class Placement(TypedDict, closed=True):
    affinity: NotRequired["aws_sdk_workspaces_instances.types.string64.String64"]
    """<p>Specifies host affinity for dedicated instances.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_workspaces_instances.types.availability_zone.AvailabilityZone"
    ]
    """<p>Identifies the specific AWS availability zone.</p>"""
    group_id: NotRequired[
        "aws_sdk_workspaces_instances.types.placement_group_id.PlacementGroupId"
    ]
    """<p>Unique identifier for placement group.</p>"""
    group_name: NotRequired["aws_sdk_workspaces_instances.types.string64.String64"]
    """<p>Name of the placement group.</p>"""
    host_id: NotRequired["aws_sdk_workspaces_instances.types.host_id.HostId"]
    """<p>Identifies the specific dedicated host.</p>"""
    host_resource_group_arn: NotRequired["aws_sdk_workspaces_instances.types.arn.ARN"]
    """<p>ARN of the host resource group.</p>"""
    partition_number: NotRequired[
        "aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Specifies partition number for partition placement groups.</p>"""
    tenancy: NotRequired["aws_sdk_workspaces_instances.types.tenancy_enum.TenancyEnum"]
    """<p>Defines instance tenancy configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Placement) -> dict:
    out: dict = {}
    if "affinity" in value:
        out["Affinity"] = value["affinity"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "host_id" in value:
        out["HostId"] = value["host_id"]
    if "host_resource_group_arn" in value:
        out["HostResourceGroupArn"] = value["host_resource_group_arn"]
    if "partition_number" in value:
        out["PartitionNumber"] = value["partition_number"]
    if "tenancy" in value:
        import aws_sdk_workspaces_instances.types.tenancy_enum

        out["Tenancy"] = (
            aws_sdk_workspaces_instances.types.tenancy_enum.serialize_aws_json_1_0(
                value["tenancy"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Placement:
    out: Placement = {}  # type: ignore[typeddict-item]
    if "Affinity" in data:
        out["affinity"] = data["Affinity"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "HostId" in data:
        out["host_id"] = data["HostId"]
    if "HostResourceGroupArn" in data:
        out["host_resource_group_arn"] = data["HostResourceGroupArn"]
    if "PartitionNumber" in data:
        out["partition_number"] = data["PartitionNumber"]
    if "Tenancy" in data:
        import aws_sdk_workspaces_instances.types.tenancy_enum

        out["tenancy"] = (
            aws_sdk_workspaces_instances.types.tenancy_enum.deserialize_aws_json_1_0(
                data["Tenancy"]
            )
        )
    return out
