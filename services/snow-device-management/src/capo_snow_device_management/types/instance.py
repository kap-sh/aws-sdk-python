"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_snow_device_management.types.cpu_options
    import capo_snow_device_management.types.instance_block_device_mapping_list
    import capo_snow_device_management.types.instance_state
    import capo_snow_device_management.types.security_group_identifier_list


class Instance(TypedDict, closed=True):
    image_id: NotRequired["str"]
    """<p>The ID of the AMI used to launch the instance.</p>"""
    ami_launch_index: NotRequired["int"]
    """<p>The Amazon Machine Image (AMI) launch index, which you can use to find this instance in the launch group. </p>"""
    instance_id: NotRequired["str"]
    """<p>The ID of the instance.</p>"""
    state: NotRequired["capo_snow_device_management.types.instance_state.InstanceState"]
    instance_type: NotRequired["str"]
    """<p>The instance type.</p>"""
    private_ip_address: NotRequired["str"]
    """<p>The private IPv4 address assigned to the instance.</p>"""
    public_ip_address: NotRequired["str"]
    """<p>The public IPv4 address assigned to the instance.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>When the instance was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>When the instance was last updated.</p>"""
    block_device_mappings: NotRequired[
        "capo_snow_device_management.types.instance_block_device_mapping_list.InstanceBlockDeviceMappingList"
    ]
    """<p>Any block device mapping entries for the instance.</p>"""
    security_groups: NotRequired[
        "capo_snow_device_management.types.security_group_identifier_list.SecurityGroupIdentifierList"
    ]
    """<p>The security groups for the instance.</p>"""
    cpu_options: NotRequired["capo_snow_device_management.types.cpu_options.CpuOptions"]
    """<p>The CPU options for the instance.</p>"""
    root_device_name: NotRequired["str"]
    """<p>The device name of the root device volume (for example, <code>/dev/sda1</code>). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Instance) -> dict:
    out: dict = {}
    if "image_id" in value:
        out["imageId"] = value["image_id"]
    if "ami_launch_index" in value:
        out["amiLaunchIndex"] = value["ami_launch_index"]
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "state" in value:
        import capo_snow_device_management.types.instance_state

        out["state"] = capo_snow_device_management.types.instance_state.serialize_json(
            value["state"]
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "private_ip_address" in value:
        out["privateIpAddress"] = value["private_ip_address"]
    if "public_ip_address" in value:
        out["publicIpAddress"] = value["public_ip_address"]
    if "created_at" in value:
        import capo_snow_device_management.types._prelude.timestamp

        out["createdAt"] = (
            capo_snow_device_management.types._prelude.timestamp.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_snow_device_management.types._prelude.timestamp

        out["updatedAt"] = (
            capo_snow_device_management.types._prelude.timestamp.serialize_json(
                value["updated_at"]
            )
        )
    if "block_device_mappings" in value:
        import capo_snow_device_management.types.instance_block_device_mapping_list

        out["blockDeviceMappings"] = (
            capo_snow_device_management.types.instance_block_device_mapping_list.serialize_json(
                value["block_device_mappings"]
            )
        )
    if "security_groups" in value:
        import capo_snow_device_management.types.security_group_identifier_list

        out["securityGroups"] = (
            capo_snow_device_management.types.security_group_identifier_list.serialize_json(
                value["security_groups"]
            )
        )
    if "cpu_options" in value:
        import capo_snow_device_management.types.cpu_options

        out["cpuOptions"] = (
            capo_snow_device_management.types.cpu_options.serialize_json(
                value["cpu_options"]
            )
        )
    if "root_device_name" in value:
        out["rootDeviceName"] = value["root_device_name"]
    return out


def deserialize_json(data: dict) -> Instance:
    out: Instance = {}  # type: ignore[typeddict-item]
    if "imageId" in data:
        out["image_id"] = data["imageId"]
    if "amiLaunchIndex" in data:
        out["ami_launch_index"] = data["amiLaunchIndex"]
    if "instanceId" in data:
        out["instance_id"] = data["instanceId"]
    if "state" in data:
        import capo_snow_device_management.types.instance_state

        out["state"] = (
            capo_snow_device_management.types.instance_state.deserialize_json(
                data["state"]
            )
        )
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "privateIpAddress" in data:
        out["private_ip_address"] = data["privateIpAddress"]
    if "publicIpAddress" in data:
        out["public_ip_address"] = data["publicIpAddress"]
    if "createdAt" in data:
        import capo_snow_device_management.types._prelude.timestamp

        out["created_at"] = (
            capo_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_snow_device_management.types._prelude.timestamp

        out["updated_at"] = (
            capo_snow_device_management.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    if "blockDeviceMappings" in data:
        import capo_snow_device_management.types.instance_block_device_mapping_list

        out["block_device_mappings"] = (
            capo_snow_device_management.types.instance_block_device_mapping_list.deserialize_json(
                data["blockDeviceMappings"]
            )
        )
    if "securityGroups" in data:
        import capo_snow_device_management.types.security_group_identifier_list

        out["security_groups"] = (
            capo_snow_device_management.types.security_group_identifier_list.deserialize_json(
                data["securityGroups"]
            )
        )
    if "cpuOptions" in data:
        import capo_snow_device_management.types.cpu_options

        out["cpu_options"] = (
            capo_snow_device_management.types.cpu_options.deserialize_json(
                data["cpuOptions"]
            )
        )
    if "rootDeviceName" in data:
        out["root_device_name"] = data["rootDeviceName"]
    return out
