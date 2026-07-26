"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicatorLogDelivery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.replicator_cloud_watch_logs
    import capo_kafka.types.replicator_firehose
    import capo_kafka.types.replicator_s3


class ReplicatorLogDelivery(TypedDict, closed=True):
    cloud_watch_logs: NotRequired[
        "capo_kafka.types.replicator_cloud_watch_logs.ReplicatorCloudWatchLogs"
    ]
    """<p>Configuration for CloudWatch Logs delivery.</p>"""
    firehose: NotRequired["capo_kafka.types.replicator_firehose.ReplicatorFirehose"]
    """<p>Configuration for Firehose delivery.</p>"""
    s3: NotRequired["capo_kafka.types.replicator_s3.ReplicatorS3"]
    """<p>Configuration for S3 delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicatorLogDelivery) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import capo_kafka.types.replicator_cloud_watch_logs

        out["cloudWatchLogs"] = (
            capo_kafka.types.replicator_cloud_watch_logs.serialize_json(
                value["cloud_watch_logs"]
            )
        )
    if "firehose" in value:
        import capo_kafka.types.replicator_firehose

        out["firehose"] = capo_kafka.types.replicator_firehose.serialize_json(
            value["firehose"]
        )
    if "s3" in value:
        import capo_kafka.types.replicator_s3

        out["s3"] = capo_kafka.types.replicator_s3.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> ReplicatorLogDelivery:
    out: ReplicatorLogDelivery = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogs" in data:
        import capo_kafka.types.replicator_cloud_watch_logs

        out["cloud_watch_logs"] = (
            capo_kafka.types.replicator_cloud_watch_logs.deserialize_json(
                data["cloudWatchLogs"]
            )
        )
    if "firehose" in data:
        import capo_kafka.types.replicator_firehose

        out["firehose"] = capo_kafka.types.replicator_firehose.deserialize_json(
            data["firehose"]
        )
    if "s3" in data:
        import capo_kafka.types.replicator_s3

        out["s3"] = capo_kafka.types.replicator_s3.deserialize_json(data["s3"])
    return out
