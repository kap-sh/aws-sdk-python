"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstancePlacementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.affinity
    import aws_sdk_ec2.types.dedicated_host_id
    import aws_sdk_ec2.types.host_tenancy
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.placement_group_id
    import aws_sdk_ec2.types.placement_group_name
    import aws_sdk_ec2.types.string


class ModifyInstancePlacementRequest(TypedDict):
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group in which to place the instance. For spread placement groups, the instance must have a tenancy of <code>default</code>. For cluster and partition placement groups, the instance must have a tenancy of <code>default</code> or <code>dedicated</code>.</p> <p>To remove an instance from a placement group, specify an empty string (\"\").</p>"""
    partition_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of the partition in which to place the instance. Valid only if the placement group strategy is set to <code>partition</code>.</p>"""
    host_resource_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the host resource group in which to place the instance. The instance must have a tenancy of <code>host</code> to specify this parameter.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>The Group Id of a placement group. You must specify the Placement Group <b>Group Id</b> to launch an instance in a shared placement group.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance that you are modifying.</p>"""
    tenancy: NotRequired["aws_sdk_ec2.types.host_tenancy.HostTenancy"]
    """<p>The tenancy for the instance.</p> <note> <p>For T3 instances, you must launch the instance on a Dedicated Host to use a tenancy of <code>host</code>. You can't change the tenancy from <code>host</code> to <code>dedicated</code> or <code>default</code>. Attempting to make one of these unsupported tenancy changes results in an <code>InvalidRequest</code> error code.</p> </note>"""
    affinity: NotRequired["aws_sdk_ec2.types.affinity.Affinity"]
    """<p>The affinity setting for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-affinity\">Host affinity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    host_id: NotRequired["aws_sdk_ec2.types.dedicated_host_id.DedicatedHostId"]
    """<p>The ID of the Dedicated Host with which to associate the instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyInstancePlacementRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    if "partition_number" in value:
        pairs.append((f"{prefix}.PartitionNumber", str(value["partition_number"])))
    if "host_resource_group_arn" in value:
        pairs.append(
            (f"{prefix}.HostResourceGroupArn", str(value["host_resource_group_arn"]))
        )
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "instance_id" in value:
        pairs.append((f"{prefix}.InstanceId", str(value["instance_id"])))
    if "tenancy" in value:
        import aws_sdk_ec2.types.host_tenancy

        aws_sdk_ec2.types.host_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{prefix}.Tenancy"
        )
    if "affinity" in value:
        import aws_sdk_ec2.types.affinity

        aws_sdk_ec2.types.affinity.serialize_ec2_query(
            value["affinity"], pairs, f"{prefix}.Affinity"
        )
    if "host_id" in value:
        pairs.append((f"{prefix}.HostId", str(value["host_id"])))


def deserialize_ec2_query(el: Element) -> ModifyInstancePlacementRequest:
    out: ModifyInstancePlacementRequest = {}  # type: ignore[typeddict-item]
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_partition_number = el.find("PartitionNumber")
    if child_partition_number is not None:
        out["partition_number"] = int(child_partition_number.text or "")
    child_host_resource_group_arn = el.find("HostResourceGroupArn")
    if child_host_resource_group_arn is not None:
        out["host_resource_group_arn"] = str(child_host_resource_group_arn.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import aws_sdk_ec2.types.host_tenancy

        out["tenancy"] = aws_sdk_ec2.types.host_tenancy.deserialize_ec2_query(
            child_tenancy
        )
    child_affinity = el.find("Affinity")
    if child_affinity is not None:
        import aws_sdk_ec2.types.affinity

        out["affinity"] = aws_sdk_ec2.types.affinity.deserialize_ec2_query(
            child_affinity
        )
    child_host_id = el.find("HostId")
    if child_host_id is not None:
        out["host_id"] = str(child_host_id.text or "")
    return out
