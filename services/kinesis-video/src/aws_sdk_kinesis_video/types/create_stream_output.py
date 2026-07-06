"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#CreateStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.resource_arn


class CreateStreamOutput(TypedDict, closed=True):
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamOutput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    return out


def deserialize_json(data: dict) -> CreateStreamOutput:
    out: CreateStreamOutput = {}  # type: ignore[typeddict-item]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    return out
