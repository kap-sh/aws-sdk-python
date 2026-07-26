"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InstanceBlockDeviceMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.ebs_instance_block_device_specification
    import capo_imagebuilder.types.empty_string
    import capo_imagebuilder.types.non_empty_string


class InstanceBlockDeviceMapping(TypedDict, closed=True):
    device_name: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The device to which these mappings apply.</p>"""
    ebs: NotRequired[
        "capo_imagebuilder.types.ebs_instance_block_device_specification.EbsInstanceBlockDeviceSpecification"
    ]
    """<p>Use to manage Amazon EBS-specific configuration for this mapping.</p>"""
    virtual_name: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Use to manage instance ephemeral devices.</p>"""
    no_device: NotRequired["capo_imagebuilder.types.empty_string.EmptyString"]
    """<p>Use to remove a mapping from the base image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceBlockDeviceMapping) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["deviceName"] = value["device_name"]
    if "ebs" in value:
        import capo_imagebuilder.types.ebs_instance_block_device_specification

        out["ebs"] = (
            capo_imagebuilder.types.ebs_instance_block_device_specification.serialize_json(
                value["ebs"]
            )
        )
    if "virtual_name" in value:
        out["virtualName"] = value["virtual_name"]
    if "no_device" in value:
        out["noDevice"] = value["no_device"]
    return out


def deserialize_json(data: dict) -> InstanceBlockDeviceMapping:
    out: InstanceBlockDeviceMapping = {}  # type: ignore[typeddict-item]
    if "deviceName" in data:
        out["device_name"] = data["deviceName"]
    if "ebs" in data:
        import capo_imagebuilder.types.ebs_instance_block_device_specification

        out["ebs"] = (
            capo_imagebuilder.types.ebs_instance_block_device_specification.deserialize_json(
                data["ebs"]
            )
        )
    if "virtualName" in data:
        out["virtual_name"] = data["virtualName"]
    if "noDevice" in data:
        out["no_device"] = data["noDevice"]
    return out
