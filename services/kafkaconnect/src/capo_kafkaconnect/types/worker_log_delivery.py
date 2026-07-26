"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerLogDelivery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.cloud_watch_logs_log_delivery
    import capo_kafkaconnect.types.firehose_log_delivery
    import capo_kafkaconnect.types.s3_log_delivery


class WorkerLogDelivery(TypedDict, closed=True):
    cloud_watch_logs: NotRequired[
        "capo_kafkaconnect.types.cloud_watch_logs_log_delivery.CloudWatchLogsLogDelivery"
    ]
    """<p>Details about delivering logs to Amazon CloudWatch Logs.</p>"""
    firehose: NotRequired[
        "capo_kafkaconnect.types.firehose_log_delivery.FirehoseLogDelivery"
    ]
    """<p>Details about delivering logs to Amazon Kinesis Data Firehose.</p>"""
    s3: NotRequired["capo_kafkaconnect.types.s3_log_delivery.S3LogDelivery"]
    """<p>Details about delivering logs to Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerLogDelivery) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import capo_kafkaconnect.types.cloud_watch_logs_log_delivery

        out["cloudWatchLogs"] = (
            capo_kafkaconnect.types.cloud_watch_logs_log_delivery.serialize_json(
                value["cloud_watch_logs"]
            )
        )
    if "firehose" in value:
        import capo_kafkaconnect.types.firehose_log_delivery

        out["firehose"] = capo_kafkaconnect.types.firehose_log_delivery.serialize_json(
            value["firehose"]
        )
    if "s3" in value:
        import capo_kafkaconnect.types.s3_log_delivery

        out["s3"] = capo_kafkaconnect.types.s3_log_delivery.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> WorkerLogDelivery:
    out: WorkerLogDelivery = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogs" in data:
        import capo_kafkaconnect.types.cloud_watch_logs_log_delivery

        out["cloud_watch_logs"] = (
            capo_kafkaconnect.types.cloud_watch_logs_log_delivery.deserialize_json(
                data["cloudWatchLogs"]
            )
        )
    if "firehose" in data:
        import capo_kafkaconnect.types.firehose_log_delivery

        out["firehose"] = (
            capo_kafkaconnect.types.firehose_log_delivery.deserialize_json(
                data["firehose"]
            )
        )
    if "s3" in data:
        import capo_kafkaconnect.types.s3_log_delivery

        out["s3"] = capo_kafkaconnect.types.s3_log_delivery.deserialize_json(data["s3"])
    return out
