"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceBlockDeviceMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ebs_instance_block_device
    import aws_sdk_ec2.types.string


class InstanceBlockDeviceMapping(TypedDict, closed=True):
    device_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The device name.</p>"""
    ebs: NotRequired[
        "aws_sdk_ec2.types.ebs_instance_block_device.EbsInstanceBlockDevice"
    ]
    """<p>Parameters used to automatically set up EBS volumes when the instance is launched.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceBlockDeviceMapping, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "device_name" in value:
        pairs.append((f"{prefix}.DeviceName", str(value["device_name"])))
    if "ebs" in value:
        import aws_sdk_ec2.types.ebs_instance_block_device

        aws_sdk_ec2.types.ebs_instance_block_device.serialize_ec2_query(
            value["ebs"], pairs, f"{prefix}.Ebs"
        )


def deserialize_ec2_query(el: Element) -> InstanceBlockDeviceMapping:
    out: InstanceBlockDeviceMapping = {}  # type: ignore[typeddict-item]
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_ebs = el.find("Ebs")
    if child_ebs is not None:
        import aws_sdk_ec2.types.ebs_instance_block_device

        out["ebs"] = aws_sdk_ec2.types.ebs_instance_block_device.deserialize_ec2_query(
            child_ebs
        )
    return out
