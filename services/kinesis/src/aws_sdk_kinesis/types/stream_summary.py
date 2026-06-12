"""Generated from Smithy shape ``com.amazonaws.kinesis#StreamSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_mode_details
    import aws_sdk_kinesis.types.stream_name
    import aws_sdk_kinesis.types.stream_status
    import aws_sdk_kinesis.types.timestamp


class StreamSummary(TypedDict):
    stream_name: "aws_sdk_kinesis.types.stream_name.StreamName"
    """<p>The name of a stream.</p>"""
    stream_arn: "aws_sdk_kinesis.types.stream_arn.StreamARN"
    """<p>The ARN of the stream.</p>"""
    stream_status: "aws_sdk_kinesis.types.stream_status.StreamStatus"
    """<p>The status of the stream.</p>"""
    stream_mode_details: NotRequired[
        "aws_sdk_kinesis.types.stream_mode_details.StreamModeDetails"
    ]
    stream_creation_timestamp: NotRequired["aws_sdk_kinesis.types.timestamp.Timestamp"]
    """<p>The timestamp at which the stream was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamSummary) -> dict:
    out: dict = {}
    out["StreamName"] = value["stream_name"]
    out["StreamARN"] = value["stream_arn"]
    import aws_sdk_kinesis.types.stream_status

    out["StreamStatus"] = aws_sdk_kinesis.types.stream_status.serialize_aws_json_1_1(
        value["stream_status"]
    )
    if "stream_mode_details" in value:
        import aws_sdk_kinesis.types.stream_mode_details

        out["StreamModeDetails"] = (
            aws_sdk_kinesis.types.stream_mode_details.serialize_aws_json_1_1(
                value["stream_mode_details"]
            )
        )
    if "stream_creation_timestamp" in value:
        import aws_sdk_kinesis.types.timestamp

        out["StreamCreationTimestamp"] = (
            aws_sdk_kinesis.types.timestamp.serialize_aws_json_1_1(
                value["stream_creation_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamSummary:
    out: StreamSummary = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    else:
        raise DeserializationError("StreamSummary.stream_name required")
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    else:
        raise DeserializationError("StreamSummary.stream_arn required")
    if "StreamStatus" in data:
        import aws_sdk_kinesis.types.stream_status

        out["stream_status"] = (
            aws_sdk_kinesis.types.stream_status.deserialize_aws_json_1_1(
                data["StreamStatus"]
            )
        )
    else:
        raise DeserializationError("StreamSummary.stream_status required")
    if "StreamModeDetails" in data:
        import aws_sdk_kinesis.types.stream_mode_details

        out["stream_mode_details"] = (
            aws_sdk_kinesis.types.stream_mode_details.deserialize_aws_json_1_1(
                data["StreamModeDetails"]
            )
        )
    if "StreamCreationTimestamp" in data:
        import aws_sdk_kinesis.types.timestamp

        out["stream_creation_timestamp"] = (
            aws_sdk_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["StreamCreationTimestamp"]
            )
        )
    return out
