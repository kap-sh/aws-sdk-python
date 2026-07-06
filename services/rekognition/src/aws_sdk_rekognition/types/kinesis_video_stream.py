"""Generated from Smithy shape ``com.amazonaws.rekognition#KinesisVideoStream``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.kinesis_video_arn


class KinesisVideoStream(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_rekognition.types.kinesis_video_arn.KinesisVideoArn"]
    """<p>ARN of the Kinesis video stream stream that streams the source video.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisVideoStream) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisVideoStream:
    out: KinesisVideoStream = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
