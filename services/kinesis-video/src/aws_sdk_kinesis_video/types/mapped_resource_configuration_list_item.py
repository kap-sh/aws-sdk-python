"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#MappedResourceConfigurationListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.type


class MappedResourceConfigurationListItem(TypedDict):
    type: NotRequired["aws_sdk_kinesis_video.types.type.Type"]
    """<p>The type of the associated resource for the kinesis video stream.</p>"""
    arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the Kinesis Video Stream resource, associated with the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MappedResourceConfigurationListItem) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "arn" in value:
        out["ARN"] = value["arn"]
    return out


def deserialize_json(data: dict) -> MappedResourceConfigurationListItem:
    out: MappedResourceConfigurationListItem = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        out["type"] = data["Type"]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    return out
