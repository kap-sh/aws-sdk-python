"""Generated from Smithy shape ``com.amazonaws.pipes#PipeLogConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.cloudwatch_logs_log_destination
    import aws_sdk_pipes.types.firehose_log_destination
    import aws_sdk_pipes.types.include_execution_data
    import aws_sdk_pipes.types.log_level
    import aws_sdk_pipes.types.s3_log_destination


class PipeLogConfiguration(TypedDict):
    s3_log_destination: NotRequired[
        "aws_sdk_pipes.types.s3_log_destination.S3LogDestination"
    ]
    """<p>The Amazon S3 logging configuration settings for the pipe.</p>"""
    firehose_log_destination: NotRequired[
        "aws_sdk_pipes.types.firehose_log_destination.FirehoseLogDestination"
    ]
    """<p>The Amazon Data Firehose logging configuration settings for the pipe.</p>"""
    cloudwatch_logs_log_destination: NotRequired[
        "aws_sdk_pipes.types.cloudwatch_logs_log_destination.CloudwatchLogsLogDestination"
    ]
    """<p>The Amazon CloudWatch Logs logging configuration settings for the pipe.</p>"""
    level: NotRequired["aws_sdk_pipes.types.log_level.LogLevel"]
    """<p>The level of logging detail to include. This applies to all log destinations for the pipe.</p>"""
    include_execution_data: NotRequired[
        "aws_sdk_pipes.types.include_execution_data.IncludeExecutionData"
    ]
    """<p>Whether the execution data (specifically, the <code>payload</code>, <code>awsRequest</code>, and <code>awsResponse</code> fields) is included in the log messages for this pipe.</p> <p>This applies to all log destinations for the pipe.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-logs.html#eb-pipes-logs-execution-data\">Including execution data in logs</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeLogConfiguration) -> dict:
    out: dict = {}
    if "s3_log_destination" in value:
        import aws_sdk_pipes.types.s3_log_destination

        out["S3LogDestination"] = aws_sdk_pipes.types.s3_log_destination.serialize_json(
            value["s3_log_destination"]
        )
    if "firehose_log_destination" in value:
        import aws_sdk_pipes.types.firehose_log_destination

        out["FirehoseLogDestination"] = (
            aws_sdk_pipes.types.firehose_log_destination.serialize_json(
                value["firehose_log_destination"]
            )
        )
    if "cloudwatch_logs_log_destination" in value:
        import aws_sdk_pipes.types.cloudwatch_logs_log_destination

        out["CloudwatchLogsLogDestination"] = (
            aws_sdk_pipes.types.cloudwatch_logs_log_destination.serialize_json(
                value["cloudwatch_logs_log_destination"]
            )
        )
    if "level" in value:
        out["Level"] = value["level"]
    if "include_execution_data" in value:
        import aws_sdk_pipes.types.include_execution_data

        out["IncludeExecutionData"] = (
            aws_sdk_pipes.types.include_execution_data.serialize_json(
                value["include_execution_data"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeLogConfiguration:
    out: PipeLogConfiguration = {}  # type: ignore[typeddict-item]
    if "S3LogDestination" in data:
        import aws_sdk_pipes.types.s3_log_destination

        out["s3_log_destination"] = (
            aws_sdk_pipes.types.s3_log_destination.deserialize_json(
                data["S3LogDestination"]
            )
        )
    if "FirehoseLogDestination" in data:
        import aws_sdk_pipes.types.firehose_log_destination

        out["firehose_log_destination"] = (
            aws_sdk_pipes.types.firehose_log_destination.deserialize_json(
                data["FirehoseLogDestination"]
            )
        )
    if "CloudwatchLogsLogDestination" in data:
        import aws_sdk_pipes.types.cloudwatch_logs_log_destination

        out["cloudwatch_logs_log_destination"] = (
            aws_sdk_pipes.types.cloudwatch_logs_log_destination.deserialize_json(
                data["CloudwatchLogsLogDestination"]
            )
        )
    if "Level" in data:
        out["level"] = data["Level"]
    if "IncludeExecutionData" in data:
        import aws_sdk_pipes.types.include_execution_data

        out["include_execution_data"] = (
            aws_sdk_pipes.types.include_execution_data.deserialize_json(
                data["IncludeExecutionData"]
            )
        )
    return out
