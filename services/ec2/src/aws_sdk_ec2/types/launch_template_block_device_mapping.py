"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateBlockDeviceMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.launch_template_ebs_block_device
    import aws_sdk_ec2.types.string


class LaunchTemplateBlockDeviceMapping(TypedDict, closed=True):
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name.</p>"""
    virtual_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The virtual device name (ephemeralN).</p>"""
    ebs: NotRequired[
        "aws_sdk_ec2.types.launch_template_ebs_block_device.LaunchTemplateEbsBlockDevice"
    ]
    """<p>Information about the block device for an EBS volume.</p>"""
    no_device: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>To omit the device from the block device mapping, specify an empty string.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateBlockDeviceMapping, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "device_name" in value:
        pairs.append((f"{prefix}.DeviceName", str(value["device_name"])))
    if "virtual_name" in value:
        pairs.append((f"{prefix}.VirtualName", str(value["virtual_name"])))
    if "ebs" in value:
        import aws_sdk_ec2.types.launch_template_ebs_block_device

        aws_sdk_ec2.types.launch_template_ebs_block_device.serialize_ec2_query(
            value["ebs"], pairs, f"{prefix}.Ebs"
        )
    if "no_device" in value:
        pairs.append((f"{prefix}.NoDevice", str(value["no_device"])))


def deserialize_ec2_query(el: Element) -> LaunchTemplateBlockDeviceMapping:
    out: LaunchTemplateBlockDeviceMapping = {}  # type: ignore[typeddict-item]
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_virtual_name = el.find("VirtualName")
    if child_virtual_name is not None:
        out["virtual_name"] = str(child_virtual_name.text or "")
    child_ebs = el.find("Ebs")
    if child_ebs is not None:
        import aws_sdk_ec2.types.launch_template_ebs_block_device

        out["ebs"] = (
            aws_sdk_ec2.types.launch_template_ebs_block_device.deserialize_ec2_query(
                child_ebs
            )
        )
    child_no_device = el.find("NoDevice")
    if child_no_device is not None:
        out["no_device"] = str(child_no_device.text or "")
    return out
