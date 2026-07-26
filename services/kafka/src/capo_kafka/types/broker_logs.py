"""Generated from Smithy shape ``com.amazonaws.kafka#BrokerLogs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.cloud_watch_logs
    import capo_kafka.types.firehose
    import capo_kafka.types.s3


class BrokerLogs(TypedDict, closed=True):
    cloud_watch_logs: NotRequired["capo_kafka.types.cloud_watch_logs.CloudWatchLogs"]
    firehose: NotRequired["capo_kafka.types.firehose.Firehose"]
    s3: NotRequired["capo_kafka.types.s3.S3"]


# --- restJson1 ser/de ---
def serialize_json(value: BrokerLogs) -> dict:
    out: dict = {}
    if "cloud_watch_logs" in value:
        import capo_kafka.types.cloud_watch_logs

        out["cloudWatchLogs"] = capo_kafka.types.cloud_watch_logs.serialize_json(
            value["cloud_watch_logs"]
        )
    if "firehose" in value:
        import capo_kafka.types.firehose

        out["firehose"] = capo_kafka.types.firehose.serialize_json(value["firehose"])
    if "s3" in value:
        import capo_kafka.types.s3

        out["s3"] = capo_kafka.types.s3.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> BrokerLogs:
    out: BrokerLogs = {}  # type: ignore[typeddict-item]
    if "cloudWatchLogs" in data:
        import capo_kafka.types.cloud_watch_logs

        out["cloud_watch_logs"] = capo_kafka.types.cloud_watch_logs.deserialize_json(
            data["cloudWatchLogs"]
        )
    if "firehose" in data:
        import capo_kafka.types.firehose

        out["firehose"] = capo_kafka.types.firehose.deserialize_json(data["firehose"])
    if "s3" in data:
        import capo_kafka.types.s3

        out["s3"] = capo_kafka.types.s3.deserialize_json(data["s3"])
    return out
