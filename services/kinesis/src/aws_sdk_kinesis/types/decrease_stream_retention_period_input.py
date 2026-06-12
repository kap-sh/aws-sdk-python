"""Generated from Smithy shape ``com.amazonaws.kinesis#DecreaseStreamRetentionPeriodInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.retention_period_hours
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_id
    import aws_sdk_kinesis.types.stream_name


class DecreaseStreamRetentionPeriodInput(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream to modify.</p>"""
    retention_period_hours: (
        "aws_sdk_kinesis.types.retention_period_hours.RetentionPeriodHours"
    )
    """<p>The new retention period of the stream, in hours. Must be less than the current retention period.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecreaseStreamRetentionPeriodInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    out["RetentionPeriodHours"] = value["retention_period_hours"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DecreaseStreamRetentionPeriodInput:
    out: DecreaseStreamRetentionPeriodInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "RetentionPeriodHours" in data:
        out["retention_period_hours"] = data["RetentionPeriodHours"]
    else:
        raise DeserializationError(
            "DecreaseStreamRetentionPeriodInput.retention_period_hours required"
        )
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
