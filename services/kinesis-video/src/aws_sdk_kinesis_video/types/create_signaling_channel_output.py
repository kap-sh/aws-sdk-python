"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#CreateSignalingChannelOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn


class CreateSignalingChannelOutput(TypedDict):
    channel_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the created channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSignalingChannelOutput) -> dict:
    out: dict = {}
    if "channel_arn" in value:
        out["ChannelARN"] = value["channel_arn"]
    return out


def deserialize_json(data: dict) -> CreateSignalingChannelOutput:
    out: CreateSignalingChannelOutput = {}  # type: ignore[typeddict-item]
    if "ChannelARN" in data:
        out["channel_arn"] = data["ChannelARN"]
    return out
