"""Generated from Smithy shape ``com.amazonaws.ec2#BlockDeviceMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ebs_block_device
    import aws_sdk_ec2.types.string


class BlockDeviceMapping(TypedDict):
    ebs: NotRequired["aws_sdk_ec2.types.ebs_block_device.EbsBlockDevice"]
    """<p>Parameters used to automatically set up EBS volumes when the instance is launched.</p>"""
    no_device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>To omit the device from the block device mapping, specify an empty string. When this property is specified, the device is removed from the block device mapping regardless of the assigned value.</p>"""
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name. For available device names, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html\">Device names for volumes</a>.</p>"""
    virtual_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The virtual device name (<code>ephemeral</code>N). Instance store volumes are numbered starting from 0. An instance type with 2 available instance store volumes can specify mappings for <code>ephemeral0</code> and <code>ephemeral1</code>. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.</p> <p>NVMe instance store volumes are automatically enumerated and assigned a device name. Including them in your block device mapping has no effect.</p> <p>Constraints: For M3 instances, you must specify instance store volumes in the block device mapping for the instance. When you launch an M3 instance, we ignore any instance store volumes specified in the block device mapping for the AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BlockDeviceMapping, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ebs" in value:
        import aws_sdk_ec2.types.ebs_block_device

        aws_sdk_ec2.types.ebs_block_device.serialize_ec2_query(
            value["ebs"], pairs, f"{prefix}.Ebs"
        )
    if "no_device" in value:
        pairs.append((f"{prefix}.NoDevice", str(value["no_device"])))
    if "device_name" in value:
        pairs.append((f"{prefix}.DeviceName", str(value["device_name"])))
    if "virtual_name" in value:
        pairs.append((f"{prefix}.VirtualName", str(value["virtual_name"])))


def deserialize_ec2_query(el: Element) -> BlockDeviceMapping:
    out: BlockDeviceMapping = {}  # type: ignore[typeddict-item]
    child_ebs = el.find("Ebs")
    if child_ebs is not None:
        import aws_sdk_ec2.types.ebs_block_device

        out["ebs"] = aws_sdk_ec2.types.ebs_block_device.deserialize_ec2_query(child_ebs)
    child_no_device = el.find("NoDevice")
    if child_no_device is not None:
        out["no_device"] = str(child_no_device.text or "")
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_virtual_name = el.find("VirtualName")
    if child_virtual_name is not None:
        out["virtual_name"] = str(child_virtual_name.text or "")
    return out
