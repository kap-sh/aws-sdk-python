"""Generated from Smithy shape ``com.amazonaws.kinesis#EnhancedMonitoringOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.metrics_name_list
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_name


class EnhancedMonitoringOutput(TypedDict, closed=True):
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the Kinesis data stream.</p>"""
    current_shard_level_metrics: NotRequired[
        "aws_sdk_kinesis.types.metrics_name_list.MetricsNameList"
    ]
    """<p>Represents the current state of the metrics that are in the enhanced state before the operation.</p>"""
    desired_shard_level_metrics: NotRequired[
        "aws_sdk_kinesis.types.metrics_name_list.MetricsNameList"
    ]
    """<p>Represents the list of all the metrics that would be in the enhanced state after the operation.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnhancedMonitoringOutput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "current_shard_level_metrics" in value:
        import aws_sdk_kinesis.types.metrics_name_list

        out["CurrentShardLevelMetrics"] = (
            aws_sdk_kinesis.types.metrics_name_list.serialize_aws_json_1_1(
                value["current_shard_level_metrics"]
            )
        )
    if "desired_shard_level_metrics" in value:
        import aws_sdk_kinesis.types.metrics_name_list

        out["DesiredShardLevelMetrics"] = (
            aws_sdk_kinesis.types.metrics_name_list.serialize_aws_json_1_1(
                value["desired_shard_level_metrics"]
            )
        )
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnhancedMonitoringOutput:
    out: EnhancedMonitoringOutput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "CurrentShardLevelMetrics" in data:
        import aws_sdk_kinesis.types.metrics_name_list

        out["current_shard_level_metrics"] = (
            aws_sdk_kinesis.types.metrics_name_list.deserialize_aws_json_1_1(
                data["CurrentShardLevelMetrics"]
            )
        )
    if "DesiredShardLevelMetrics" in data:
        import aws_sdk_kinesis.types.metrics_name_list

        out["desired_shard_level_metrics"] = (
            aws_sdk_kinesis.types.metrics_name_list.deserialize_aws_json_1_1(
                data["DesiredShardLevelMetrics"]
            )
        )
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    return out
