"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointBufferingHints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.http_endpoint_buffering_interval_in_seconds
    import capo_firehose.types.http_endpoint_buffering_size_in_m_bs


class HttpEndpointBufferingHints(TypedDict, closed=True):
    size_in_m_bs: NotRequired[
        "capo_firehose.types.http_endpoint_buffering_size_in_m_bs.HttpEndpointBufferingSizeInMBs"
    ]
    """<p>Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. </p> <p>We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher. </p>"""
    interval_in_seconds: NotRequired[
        "capo_firehose.types.http_endpoint_buffering_interval_in_seconds.HttpEndpointBufferingIntervalInSeconds"
    ]
    """<p>Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointBufferingHints) -> dict:
    out: dict = {}
    if "size_in_m_bs" in value:
        out["SizeInMBs"] = value["size_in_m_bs"]
    if "interval_in_seconds" in value:
        out["IntervalInSeconds"] = value["interval_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpEndpointBufferingHints:
    out: HttpEndpointBufferingHints = {}  # type: ignore[typeddict-item]
    if "SizeInMBs" in data:
        out["size_in_m_bs"] = data["SizeInMBs"]
    if "IntervalInSeconds" in data:
        out["interval_in_seconds"] = data["IntervalInSeconds"]
    return out
