"""Generated from Smithy shape ``com.amazonaws.rekognition#StreamProcessorOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.kinesis_data_stream
    import capo_rekognition.types.s3_destination


class StreamProcessorOutput(TypedDict, closed=True):
    kinesis_data_stream: NotRequired[
        "capo_rekognition.types.kinesis_data_stream.KinesisDataStream"
    ]
    """<p>The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams the analysis results.</p>"""
    s3_destination: NotRequired["capo_rekognition.types.s3_destination.S3Destination"]
    """<p> The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamProcessorOutput) -> dict:
    out: dict = {}
    if "kinesis_data_stream" in value:
        import capo_rekognition.types.kinesis_data_stream

        out["KinesisDataStream"] = (
            capo_rekognition.types.kinesis_data_stream.serialize_aws_json_1_1(
                value["kinesis_data_stream"]
            )
        )
    if "s3_destination" in value:
        import capo_rekognition.types.s3_destination

        out["S3Destination"] = (
            capo_rekognition.types.s3_destination.serialize_aws_json_1_1(
                value["s3_destination"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamProcessorOutput:
    out: StreamProcessorOutput = {}  # type: ignore[typeddict-item]
    if "KinesisDataStream" in data:
        import capo_rekognition.types.kinesis_data_stream

        out["kinesis_data_stream"] = (
            capo_rekognition.types.kinesis_data_stream.deserialize_aws_json_1_1(
                data["KinesisDataStream"]
            )
        )
    if "S3Destination" in data:
        import capo_rekognition.types.s3_destination

        out["s3_destination"] = (
            capo_rekognition.types.s3_destination.deserialize_aws_json_1_1(
                data["S3Destination"]
            )
        )
    return out
