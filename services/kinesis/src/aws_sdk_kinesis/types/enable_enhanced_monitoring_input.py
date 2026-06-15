"""Generated from Smithy shape ``com.amazonaws.kinesis#EnableEnhancedMonitoringInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.metrics_name_list
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_id
    import aws_sdk_kinesis.types.stream_name


class EnableEnhancedMonitoringInput(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream for which to enable enhanced monitoring.</p>"""
    shard_level_metrics: "aws_sdk_kinesis.types.metrics_name_list.MetricsNameList"
    r"""<p>List of shard-level metrics to enable.</p> <p>The following are the valid shard-level metrics. The value \"<code>ALL</code>\" enables every metric.</p> <ul> <li> <p> <code>IncomingBytes</code> </p> </li> <li> <p> <code>IncomingRecords</code> </p> </li> <li> <p> <code>OutgoingBytes</code> </p> </li> <li> <p> <code>OutgoingRecords</code> </p> </li> <li> <p> <code>WriteProvisionedThroughputExceeded</code> </p> </li> <li> <p> <code>ReadProvisionedThroughputExceeded</code> </p> </li> <li> <p> <code>IteratorAgeMilliseconds</code> </p> </li> <li> <p> <code>ALL</code> </p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html\">Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableEnhancedMonitoringInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    import aws_sdk_kinesis.types.metrics_name_list

    out["ShardLevelMetrics"] = (
        aws_sdk_kinesis.types.metrics_name_list.serialize_aws_json_1_1(
            value["shard_level_metrics"]
        )
    )
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableEnhancedMonitoringInput:
    out: EnableEnhancedMonitoringInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "ShardLevelMetrics" in data:
        import aws_sdk_kinesis.types.metrics_name_list

        out["shard_level_metrics"] = (
            aws_sdk_kinesis.types.metrics_name_list.deserialize_aws_json_1_1(
                data["ShardLevelMetrics"]
            )
        )
    else:
        raise DeserializationError(
            "EnableEnhancedMonitoringInput.shard_level_metrics required"
        )
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
