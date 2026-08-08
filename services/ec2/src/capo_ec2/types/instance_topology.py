"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTopology``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_nodes_list
    import capo_ec2.types.string


class InstanceTopology(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance ID.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    group_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the placement group that the instance is in.</p>"""
    network_nodes: NotRequired["capo_ec2.types.network_nodes_list.NetworkNodesList"]
    """<p>The network nodes. The nodes are hashed based on your account. Instances from different accounts running under the same server will return a different hashed list of strings.</p> <p>The value is <code>null</code> or empty if:</p> <ul> <li> <p>The instance type is not supported.</p> </li> <li> <p>The instance is in a state other than <code>running</code>.</p> </li> </ul>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the Availability Zone or Local Zone that the instance is in.</p>"""
    zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone or Local Zone that the instance is in.</p>"""
    capacity_block_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Capacity Block. This parameter is only supported for UltraServer instances and identifies instances within the UltraServer domain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceTopology, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "network_nodes" in value:
        import capo_ec2.types.network_nodes_list

        capo_ec2.types.network_nodes_list.serialize_ec2_query(
            value["network_nodes"], pairs, f"{key_prefix}NetworkNodeSet"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "zone_id" in value:
        pairs.append((f"{key_prefix}ZoneId", str(value["zone_id"])))
    if "capacity_block_id" in value:
        pairs.append((f"{key_prefix}CapacityBlockId", str(value["capacity_block_id"])))


def deserialize_ec2_query(el: Element) -> InstanceTopology:
    out: InstanceTopology = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_group_name = el.find("groupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    if el.find("networkNodeSet") is not None:
        import capo_ec2.types.network_nodes_list

        out["network_nodes"] = capo_ec2.types.network_nodes_list.deserialize_ec2_query(
            el, "networkNodeSet"
        )
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_zone_id = el.find("zoneId")
    if child_zone_id is not None:
        out["zone_id"] = str(child_zone_id.text or "")
    child_capacity_block_id = el.find("capacityBlockId")
    if child_capacity_block_id is not None:
        out["capacity_block_id"] = str(child_capacity_block_id.text or "")
    return out
