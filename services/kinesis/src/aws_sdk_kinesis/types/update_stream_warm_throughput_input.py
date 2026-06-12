"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateStreamWarmThroughputInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.natural_integer_object
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_id
    import aws_sdk_kinesis.types.stream_name


class UpdateStreamWarmThroughputInput(TypedDict):
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream to be updated.</p>"""
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream to be updated.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""
    warm_throughput_mi_bps: (
        "aws_sdk_kinesis.types.natural_integer_object.NaturalIntegerObject"
    )
    """<p>The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStreamWarmThroughputInput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    out["WarmThroughputMiBps"] = value["warm_throughput_mi_bps"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStreamWarmThroughputInput:
    out: UpdateStreamWarmThroughputInput = {}  # type: ignore[typeddict-item]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    if "WarmThroughputMiBps" in data:
        out["warm_throughput_mi_bps"] = data["WarmThroughputMiBps"]
    else:
        raise DeserializationError(
            "UpdateStreamWarmThroughputInput.warm_throughput_mi_bps required"
        )
    return out
