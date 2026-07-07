"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplatePlacementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.dedicated_host_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.placement_group_id
    import aws_sdk_ec2.types.placement_group_name
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tenancy


class LaunchTemplatePlacementRequest(TypedDict, closed=True):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone for the instance.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone for the instance.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    affinity: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The affinity setting for an instance on a Dedicated Host.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group for the instance.</p>"""
    host_id: NotRequired["aws_sdk_ec2.types.dedicated_host_id.DedicatedHostId"]
    """<p>The ID of the Dedicated Host for the instance.</p>"""
    tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance. An instance with a tenancy of dedicated runs on single-tenant hardware.</p>"""
    spread_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved for future use.</p>"""
    host_resource_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the host resource group in which to launch the instances. If you specify a host resource group ARN, omit the <b>Tenancy</b> parameter or set it to <code>host</code>.</p>"""
    partition_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of the partition the instance should launch in. Valid only if the placement group strategy is set to <code>partition</code>.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>The Group Id of a placement group. You must specify the Placement Group <b>Group Id</b> to launch an instance in a shared placement group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplatePlacementRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "affinity" in value:
        pairs.append((f"{prefix}.Affinity", str(value["affinity"])))
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    if "host_id" in value:
        pairs.append((f"{prefix}.HostId", str(value["host_id"])))
    if "tenancy" in value:
        import aws_sdk_ec2.types.tenancy

        aws_sdk_ec2.types.tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{prefix}.Tenancy"
        )
    if "spread_domain" in value:
        pairs.append((f"{prefix}.SpreadDomain", str(value["spread_domain"])))
    if "host_resource_group_arn" in value:
        pairs.append(
            (f"{prefix}.HostResourceGroupArn", str(value["host_resource_group_arn"]))
        )
    if "partition_number" in value:
        pairs.append((f"{prefix}.PartitionNumber", str(value["partition_number"])))
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))


def deserialize_ec2_query(el: Element) -> LaunchTemplatePlacementRequest:
    out: LaunchTemplatePlacementRequest = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_affinity = el.find("Affinity")
    if child_affinity is not None:
        out["affinity"] = str(child_affinity.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_host_id = el.find("HostId")
    if child_host_id is not None:
        out["host_id"] = str(child_host_id.text or "")
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import aws_sdk_ec2.types.tenancy

        out["tenancy"] = aws_sdk_ec2.types.tenancy.deserialize_ec2_query(child_tenancy)
    child_spread_domain = el.find("SpreadDomain")
    if child_spread_domain is not None:
        out["spread_domain"] = str(child_spread_domain.text or "")
    child_host_resource_group_arn = el.find("HostResourceGroupArn")
    if child_host_resource_group_arn is not None:
        out["host_resource_group_arn"] = str(child_host_resource_group_arn.text or "")
    child_partition_number = el.find("PartitionNumber")
    if child_partition_number is not None:
        out["partition_number"] = int(child_partition_number.text or "")
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    return out
