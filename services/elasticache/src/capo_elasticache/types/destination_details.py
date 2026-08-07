"""Generated from Smithy shape ``com.amazonaws.elasticache#DestinationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cloud_watch_logs_destination_details
    import capo_elasticache.types.kinesis_firehose_destination_details


class DestinationDetails(TypedDict, closed=True):
    cloud_watch_logs_details: NotRequired[
        "capo_elasticache.types.cloud_watch_logs_destination_details.CloudWatchLogsDestinationDetails"
    ]
    """<p>The configuration details of the CloudWatch Logs destination.</p>"""
    kinesis_firehose_details: NotRequired[
        "capo_elasticache.types.kinesis_firehose_destination_details.KinesisFirehoseDestinationDetails"
    ]
    """<p>The configuration details of the Kinesis Data Firehose destination.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DestinationDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cloud_watch_logs_details" in value:
        import capo_elasticache.types.cloud_watch_logs_destination_details

        capo_elasticache.types.cloud_watch_logs_destination_details.serialize_query(
            value["cloud_watch_logs_details"],
            pairs,
            f"{key_prefix}CloudWatchLogsDetails",
        )
    if "kinesis_firehose_details" in value:
        import capo_elasticache.types.kinesis_firehose_destination_details

        capo_elasticache.types.kinesis_firehose_destination_details.serialize_query(
            value["kinesis_firehose_details"],
            pairs,
            f"{key_prefix}KinesisFirehoseDetails",
        )


def deserialize_query(el: Element) -> DestinationDetails:
    out: DestinationDetails = {}  # type: ignore[typeddict-item]
    child_cloud_watch_logs_details = el.find("CloudWatchLogsDetails")
    if child_cloud_watch_logs_details is not None:
        import capo_elasticache.types.cloud_watch_logs_destination_details

        out["cloud_watch_logs_details"] = (
            capo_elasticache.types.cloud_watch_logs_destination_details.deserialize_query(
                child_cloud_watch_logs_details
            )
        )
    child_kinesis_firehose_details = el.find("KinesisFirehoseDetails")
    if child_kinesis_firehose_details is not None:
        import capo_elasticache.types.kinesis_firehose_destination_details

        out["kinesis_firehose_details"] = (
            capo_elasticache.types.kinesis_firehose_destination_details.deserialize_query(
                child_kinesis_firehose_details
            )
        )
    return out
