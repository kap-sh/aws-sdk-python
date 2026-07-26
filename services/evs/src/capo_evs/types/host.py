"""Generated from Smithy shape ``com.amazonaws.evs#Host``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_evs.types.dedicated_host_id
    import capo_evs.types.host_name
    import capo_evs.types.host_state
    import capo_evs.types.instance_type
    import capo_evs.types.ip_address
    import capo_evs.types.key_name
    import capo_evs.types.network_interface_list
    import capo_evs.types.placement_group_id
    import capo_evs.types.state_details


class Host(TypedDict, closed=True):
    host_name: NotRequired["capo_evs.types.host_name.HostName"]
    """<p>The DNS hostname of the host. DNS hostnames for hosts must be unique across Amazon EVS environments and within VCF.</p>"""
    ip_address: NotRequired["capo_evs.types.ip_address.IpAddress"]
    """<p>The IP address of the host.</p>"""
    key_name: NotRequired["capo_evs.types.key_name.KeyName"]
    """<p>The name of the SSH key that is used to access the host.</p>"""
    instance_type: NotRequired["capo_evs.types.instance_type.InstanceType"]
    """<p>The EC2 instance type of the host.</p> <note> <p>EC2 instances created through Amazon EVS do not support associating an IAM instance profile.</p> </note>"""
    placement_group_id: NotRequired[
        "capo_evs.types.placement_group_id.PlacementGroupId"
    ]
    """<p>The unique ID of the placement group where the host is placed.</p>"""
    dedicated_host_id: NotRequired["capo_evs.types.dedicated_host_id.DedicatedHostId"]
    """<p>The unique ID of the Amazon EC2 Dedicated Host.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The date and time that the host was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p> The date and time that the host was modified.</p>"""
    host_state: NotRequired["capo_evs.types.host_state.HostState"]
    """<p> The state of the host.</p>"""
    state_details: NotRequired["capo_evs.types.state_details.StateDetails"]
    """<p> A detailed description of the <code>hostState</code> of a host.</p>"""
    ec2_instance_id: NotRequired["str"]
    """<p>The unique ID of the EC2 instance that represents the host.</p>"""
    network_interfaces: NotRequired[
        "capo_evs.types.network_interface_list.NetworkInterfaceList"
    ]
    """<p>The elastic network interfaces that are attached to the host.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Host) -> dict:
    out: dict = {}
    if "host_name" in value:
        out["hostName"] = value["host_name"]
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "key_name" in value:
        out["keyName"] = value["key_name"]
    if "instance_type" in value:
        import capo_evs.types.instance_type

        out["instanceType"] = capo_evs.types.instance_type.serialize_aws_json_1_0(
            value["instance_type"]
        )
    if "placement_group_id" in value:
        out["placementGroupId"] = value["placement_group_id"]
    if "dedicated_host_id" in value:
        out["dedicatedHostId"] = value["dedicated_host_id"]
    if "created_at" in value:
        import capo_evs.types._prelude.timestamp

        out["createdAt"] = capo_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "modified_at" in value:
        import capo_evs.types._prelude.timestamp

        out["modifiedAt"] = capo_evs.types._prelude.timestamp.serialize_aws_json_1_0(
            value["modified_at"]
        )
    if "host_state" in value:
        import capo_evs.types.host_state

        out["hostState"] = capo_evs.types.host_state.serialize_aws_json_1_0(
            value["host_state"]
        )
    if "state_details" in value:
        out["stateDetails"] = value["state_details"]
    if "ec2_instance_id" in value:
        out["ec2InstanceId"] = value["ec2_instance_id"]
    if "network_interfaces" in value:
        import capo_evs.types.network_interface_list

        out["networkInterfaces"] = (
            capo_evs.types.network_interface_list.serialize_aws_json_1_0(
                value["network_interfaces"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Host:
    out: Host = {}  # type: ignore[typeddict-item]
    if "hostName" in data:
        out["host_name"] = data["hostName"]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "keyName" in data:
        out["key_name"] = data["keyName"]
    if "instanceType" in data:
        import capo_evs.types.instance_type

        out["instance_type"] = capo_evs.types.instance_type.deserialize_aws_json_1_0(
            data["instanceType"]
        )
    if "placementGroupId" in data:
        out["placement_group_id"] = data["placementGroupId"]
    if "dedicatedHostId" in data:
        out["dedicated_host_id"] = data["dedicatedHostId"]
    if "createdAt" in data:
        import capo_evs.types._prelude.timestamp

        out["created_at"] = capo_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    if "modifiedAt" in data:
        import capo_evs.types._prelude.timestamp

        out["modified_at"] = capo_evs.types._prelude.timestamp.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    if "hostState" in data:
        import capo_evs.types.host_state

        out["host_state"] = capo_evs.types.host_state.deserialize_aws_json_1_0(
            data["hostState"]
        )
    if "stateDetails" in data:
        out["state_details"] = data["stateDetails"]
    if "ec2InstanceId" in data:
        out["ec2_instance_id"] = data["ec2InstanceId"]
    if "networkInterfaces" in data:
        import capo_evs.types.network_interface_list

        out["network_interfaces"] = (
            capo_evs.types.network_interface_list.deserialize_aws_json_1_0(
                data["networkInterfaces"]
            )
        )
    return out
