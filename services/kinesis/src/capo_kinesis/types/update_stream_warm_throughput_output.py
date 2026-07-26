"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateStreamWarmThroughputOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.warm_throughput_object


class UpdateStreamWarmThroughputOutput(TypedDict, closed=True):
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream that was updated.</p>"""
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream that was updated.</p>"""
    warm_throughput: NotRequired[
        "capo_kinesis.types.warm_throughput_object.WarmThroughputObject"
    ]
    """<p>Specifies the updated warm throughput configuration for your data stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStreamWarmThroughputOutput) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "warm_throughput" in value:
        import capo_kinesis.types.warm_throughput_object

        out["WarmThroughput"] = (
            capo_kinesis.types.warm_throughput_object.serialize_aws_json_1_1(
                value["warm_throughput"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStreamWarmThroughputOutput:
    out: UpdateStreamWarmThroughputOutput = {}  # type: ignore[typeddict-item]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "WarmThroughput" in data:
        import capo_kinesis.types.warm_throughput_object

        out["warm_throughput"] = (
            capo_kinesis.types.warm_throughput_object.deserialize_aws_json_1_1(
                data["WarmThroughput"]
            )
        )
    return out
