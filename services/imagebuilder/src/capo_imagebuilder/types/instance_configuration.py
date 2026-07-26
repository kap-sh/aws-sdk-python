"""Generated from Smithy shape ``com.amazonaws.imagebuilder#InstanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.instance_block_device_mappings
    import capo_imagebuilder.types.non_empty_string


class InstanceConfiguration(TypedDict, closed=True):
    image: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The base image for a container build and test instance. This can contain an AMI ID or it can specify an Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by <code>ssm:</code>, followed by the parameter name or ARN.</p> <p>If not specified, Image Builder uses the appropriate ECS-optimized AMI as a base image.</p>"""
    block_device_mappings: NotRequired[
        "capo_imagebuilder.types.instance_block_device_mappings.InstanceBlockDeviceMappings"
    ]
    """<p>Defines the block devices to attach for building an instance from this Image Builder AMI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceConfiguration) -> dict:
    out: dict = {}
    if "image" in value:
        out["image"] = value["image"]
    if "block_device_mappings" in value:
        import capo_imagebuilder.types.instance_block_device_mappings

        out["blockDeviceMappings"] = (
            capo_imagebuilder.types.instance_block_device_mappings.serialize_json(
                value["block_device_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> InstanceConfiguration:
    out: InstanceConfiguration = {}  # type: ignore[typeddict-item]
    if "image" in data:
        out["image"] = data["image"]
    if "blockDeviceMappings" in data:
        import capo_imagebuilder.types.instance_block_device_mappings

        out["block_device_mappings"] = (
            capo_imagebuilder.types.instance_block_device_mappings.deserialize_json(
                data["blockDeviceMappings"]
            )
        )
    return out
