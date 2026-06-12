"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerLogDelivery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery
    import aws_sdk_kafkaconnect.types.firehose_log_delivery
    import aws_sdk_kafkaconnect.types.s3_log_delivery


class WorkerLogDelivery(TypedDict):
    cloud_watch_logs: NotRequired[
        "aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery.CloudWatchLogsLogDelivery"
    ]
    """<p>Details about delivering logs to Amazon CloudWatch Logs.</p>"""
    firehose: NotRequired[
        "aws_sdk_kafkaconnect.types.firehose_log_delivery.FirehoseLogDelivery"
    ]
    """<p>Details about delivering logs to Amazon Kinesis Data Firehose.</p>"""
    s3: NotRequired["aws_sdk_kafkaconnect.types.s3_log_delivery.S3LogDelivery"]
    """<p>Details about delivering logs to Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerLogDelivery) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery

        out["cloudWatchLogs"] = (
            aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery.serialize_json(
                value["cloud_watch_logs"]
            )
        )
    if "firehose" in value:
        import aws_sdk_kafkaconnect.types.firehose_log_delivery

        out["firehose"] = (
            aws_sdk_kafkaconnect.types.firehose_log_delivery.serialize_json(
                value["firehose"]
            )
        )
    if "s3" in value:
        import aws_sdk_kafkaconnect.types.s3_log_delivery

        out["s3"] = aws_sdk_kafkaconnect.types.s3_log_delivery.serialize_json(
            value["s3"]
        )
    return out


def deserialize_json(data: dict) -> WorkerLogDelivery:
    out: WorkerLogDelivery = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogs" in data:
        import aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery

        out["cloud_watch_logs"] = (
            aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery.deserialize_json(
                data["cloudWatchLogs"]
            )
        )
    if "firehose" in data:
        import aws_sdk_kafkaconnect.types.firehose_log_delivery

        out["firehose"] = (
            aws_sdk_kafkaconnect.types.firehose_log_delivery.deserialize_json(
                data["firehose"]
            )
        )
    if "s3" in data:
        import aws_sdk_kafkaconnect.types.s3_log_delivery

        out["s3"] = aws_sdk_kafkaconnect.types.s3_log_delivery.deserialize_json(
            data["s3"]
        )
    return out
