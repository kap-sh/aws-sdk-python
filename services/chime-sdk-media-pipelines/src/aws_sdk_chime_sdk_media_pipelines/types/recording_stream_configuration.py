"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#RecordingStreamConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_arn


class RecordingStreamConfiguration(TypedDict):
    stream_arn: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.kinesis_video_stream_arn.KinesisVideoStreamArn"
    ]
    """<p>The ARN of the recording stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordingStreamConfiguration) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamArn"] = value["stream_arn"]
    return out


def deserialize_json(data: dict) -> RecordingStreamConfiguration:
    out: RecordingStreamConfiguration = {}  # type: ignore[typeddict-item]
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    return out
