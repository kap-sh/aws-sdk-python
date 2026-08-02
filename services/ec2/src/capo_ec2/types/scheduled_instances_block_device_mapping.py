"""Generated from Smithy shape ``com.amazonaws.ec2#ScheduledInstancesBlockDeviceMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.scheduled_instances_ebs
    import capo_ec2.types.string


class ScheduledInstancesBlockDeviceMapping(TypedDict, closed=True):
    device_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The device name (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p>"""
    ebs: NotRequired["capo_ec2.types.scheduled_instances_ebs.ScheduledInstancesEbs"]
    """<p>Parameters used to set up EBS volumes automatically when the instance is launched.</p>"""
    no_device: NotRequired["capo_ec2.types.string.String"]
    """<p>To omit the device from the block device mapping, specify an empty string.</p>"""
    virtual_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The virtual device name (<code>ephemeral</code>N). Instance store volumes are numbered starting from 0. An instance type with two available instance store volumes can specify mappings for <code>ephemeral0</code> and <code>ephemeral1</code>. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.</p> <p>Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ScheduledInstancesBlockDeviceMapping,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "device_name" in value:
        pairs.append((f"{key_prefix}DeviceName", str(value["device_name"])))
    if "ebs" in value:
        import capo_ec2.types.scheduled_instances_ebs

        capo_ec2.types.scheduled_instances_ebs.serialize_ec2_query(
            value["ebs"], pairs, f"{key_prefix}Ebs"
        )
    if "no_device" in value:
        pairs.append((f"{key_prefix}NoDevice", str(value["no_device"])))
    if "virtual_name" in value:
        pairs.append((f"{key_prefix}VirtualName", str(value["virtual_name"])))


def deserialize_ec2_query(el: Element) -> ScheduledInstancesBlockDeviceMapping:
    out: ScheduledInstancesBlockDeviceMapping = {}  # type: ignore[typeddict-item]
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_ebs = el.find("Ebs")
    if child_ebs is not None:
        import capo_ec2.types.scheduled_instances_ebs

        out["ebs"] = capo_ec2.types.scheduled_instances_ebs.deserialize_ec2_query(
            child_ebs
        )
    child_no_device = el.find("NoDevice")
    if child_no_device is not None:
        out["no_device"] = str(child_no_device.text or "")
    child_virtual_name = el.find("VirtualName")
    if child_virtual_name is not None:
        out["virtual_name"] = str(child_virtual_name.text or "")
    return out
