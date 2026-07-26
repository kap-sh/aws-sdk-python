"""Generated from Smithy shape ``com.amazonaws.rekognition#KinesisDataStream``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.kinesis_data_arn


class KinesisDataStream(TypedDict, closed=True):
    arn: NotRequired["capo_rekognition.types.kinesis_data_arn.KinesisDataArn"]
    """<p>ARN of the output Amazon Kinesis Data Streams stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisDataStream) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisDataStream:
    out: KinesisDataStream = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
