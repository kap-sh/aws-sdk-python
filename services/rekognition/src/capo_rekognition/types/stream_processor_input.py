"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.kinesis_video_stream


class StreamProcessorInput(TypedDict, closed=True):
    kinesis_video_stream: NotRequired[
        "capo_rekognition.types.kinesis_video_stream.KinesisVideoStream"
    ]
    """<p>The Kinesis video stream input stream for the source streaming video.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorInput) -> dict:
    out: dict = {}
    if "kinesis_video_stream" in value:
        import capo_rekognition.types.kinesis_video_stream

        out["KinesisVideoStream"] = (
            capo_rekognition.types.kinesis_video_stream.serialize_aws_json_1_1(
                value["kinesis_video_stream"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessorInput:
    out: StreamProcessorInput = {}  # type: ignore[typeddict-item]
    if "KinesisVideoStream" in data:
        import capo_rekognition.types.kinesis_video_stream

        out["kinesis_video_stream"] = (
            capo_rekognition.types.kinesis_video_stream.deserialize_aws_json_1_1(
                data["KinesisVideoStream"]
            )
        )
    return out
