"""Generated from Smithy shape ``com.amazonaws.firehose#SplunkBufferingHints``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.splunk_buffering_interval_in_seconds
    import aws_sdk_firehose.types.splunk_buffering_size_in_m_bs


class SplunkBufferingHints(TypedDict):
    interval_in_seconds: NotRequired[
        "aws_sdk_firehose.types.splunk_buffering_interval_in_seconds.SplunkBufferingIntervalInSeconds"
    ]
    """<p>Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 60 (1 minute).</p>"""
    size_in_m_bs: NotRequired[
        "aws_sdk_firehose.types.splunk_buffering_size_in_m_bs.SplunkBufferingSizeInMBs"
    ]
    """<p>Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplunkBufferingHints) -> dict:
    out: dict = {}
    if "interval_in_seconds" in value:
        out["IntervalInSeconds"] = value["interval_in_seconds"]
    if "size_in_m_bs" in value:
        out["SizeInMBs"] = value["size_in_m_bs"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SplunkBufferingHints:
    out: SplunkBufferingHints = {}  # type: ignore[typeddict-item]
    if "IntervalInSeconds" in data:
        out["interval_in_seconds"] = data["IntervalInSeconds"]
    if "SizeInMBs" in data:
        out["size_in_m_bs"] = data["SizeInMBs"]
    return out
