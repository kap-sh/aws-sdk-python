"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerLogDeliveryDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery_description
    import aws_sdk_kafkaconnect.types.firehose_log_delivery_description
    import aws_sdk_kafkaconnect.types.s3_log_delivery_description


class WorkerLogDeliveryDescription(TypedDict, closed=True):
    cloud_watch_logs: NotRequired[
        "aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery_description.CloudWatchLogsLogDeliveryDescription"
    ]
    """<p>Details about delivering logs to Amazon CloudWatch Logs.</p>"""
    firehose: NotRequired[
        "aws_sdk_kafkaconnect.types.firehose_log_delivery_description.FirehoseLogDeliveryDescription"
    ]
    """<p>Details about delivering logs to Amazon Kinesis Data Firehose.</p>"""
    s3: NotRequired[
        "aws_sdk_kafkaconnect.types.s3_log_delivery_description.S3LogDeliveryDescription"
    ]
    """<p>Details about delivering logs to Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerLogDeliveryDescription) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery_description

        out["cloudWatchLogs"] = (
            aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery_description.serialize_json(
                value["cloud_watch_logs"]
            )
        )
    if "firehose" in value:
        import aws_sdk_kafkaconnect.types.firehose_log_delivery_description

        out["firehose"] = (
            aws_sdk_kafkaconnect.types.firehose_log_delivery_description.serialize_json(
                value["firehose"]
            )
        )
    if "s3" in value:
        import aws_sdk_kafkaconnect.types.s3_log_delivery_description

        out["s3"] = (
            aws_sdk_kafkaconnect.types.s3_log_delivery_description.serialize_json(
                value["s3"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkerLogDeliveryDescription:
    out: WorkerLogDeliveryDescription = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogs" in data:
        import aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery_description

        out["cloud_watch_logs"] = (
            aws_sdk_kafkaconnect.types.cloud_watch_logs_log_delivery_description.deserialize_json(
                data["cloudWatchLogs"]
            )
        )
    if "firehose" in data:
        import aws_sdk_kafkaconnect.types.firehose_log_delivery_description

        out["firehose"] = (
            aws_sdk_kafkaconnect.types.firehose_log_delivery_description.deserialize_json(
                data["firehose"]
            )
        )
    if "s3" in data:
        import aws_sdk_kafkaconnect.types.s3_log_delivery_description

        out["s3"] = (
            aws_sdk_kafkaconnect.types.s3_log_delivery_description.deserialize_json(
                data["s3"]
            )
        )
    return out
