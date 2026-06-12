"""Generated from Smithy shape ``com.amazonaws.firehose#ElasticsearchBufferingHints``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.elasticsearch_buffering_interval_in_seconds
    import aws_sdk_firehose.types.elasticsearch_buffering_size_in_m_bs


class ElasticsearchBufferingHints(TypedDict):
    interval_in_seconds: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_buffering_interval_in_seconds.ElasticsearchBufferingIntervalInSeconds"
    ]
    """<p>Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).</p>"""
    size_in_m_bs: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_buffering_size_in_m_bs.ElasticsearchBufferingSizeInMBs"
    ]
    """<p>Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.</p> <p>We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElasticsearchBufferingHints) -> dict:
    out: dict = {}
    if "interval_in_seconds" in value:
        out["IntervalInSeconds"] = value["interval_in_seconds"]
    if "size_in_m_bs" in value:
        out["SizeInMBs"] = value["size_in_m_bs"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ElasticsearchBufferingHints:
    out: ElasticsearchBufferingHints = {}  # type: ignore[typeddict-item]
    if "IntervalInSeconds" in data:
        out["interval_in_seconds"] = data["IntervalInSeconds"]
    if "SizeInMBs" in data:
        out["size_in_m_bs"] = data["SizeInMBs"]
    return out
