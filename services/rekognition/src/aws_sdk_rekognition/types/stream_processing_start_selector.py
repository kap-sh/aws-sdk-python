"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessingStartSelector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.kinesis_video_stream_start_selector


class StreamProcessingStartSelector(TypedDict, closed=True):
    kvs_stream_start_selector: NotRequired[
        "aws_sdk_rekognition.types.kinesis_video_stream_start_selector.KinesisVideoStreamStartSelector"
    ]
    """<p> Specifies the starting point in the stream to start processing. This can be done with a producer timestamp or a fragment number in a Kinesis stream. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessingStartSelector) -> dict:
    out: dict = {}
    if "kvs_stream_start_selector" in value:
        import aws_sdk_rekognition.types.kinesis_video_stream_start_selector

        out["KVSStreamStartSelector"] = (
            aws_sdk_rekognition.types.kinesis_video_stream_start_selector.serialize_aws_json_1_1(
                value["kvs_stream_start_selector"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessingStartSelector:
    out: StreamProcessingStartSelector = {}  # type: ignore[typeddict-item]
    if "KVSStreamStartSelector" in data:
        import aws_sdk_rekognition.types.kinesis_video_stream_start_selector

        out["kvs_stream_start_selector"] = (
            aws_sdk_rekognition.types.kinesis_video_stream_start_selector.deserialize_aws_json_1_1(
                data["KVSStreamStartSelector"]
            )
        )
    return out
