"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeBufferingHints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_firehose.types.snowflake_buffering_interval_in_seconds
    import aws_sdk_firehose.types.snowflake_buffering_size_in_m_bs


class SnowflakeBufferingHints(TypedDict, closed=True):
    size_in_m_bs: NotRequired[
        "aws_sdk_firehose.types.snowflake_buffering_size_in_m_bs.SnowflakeBufferingSizeInMBs"
    ]
    """<p>Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 128. </p>"""
    interval_in_seconds: NotRequired[
        "aws_sdk_firehose.types.snowflake_buffering_interval_in_seconds.SnowflakeBufferingIntervalInSeconds"
    ]
    """<p> Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 0. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeBufferingHints) -> dict:
    out: dict = {}
    if "size_in_m_bs" in value:
        out["SizeInMBs"] = value["size_in_m_bs"]
    if "interval_in_seconds" in value:
        out["IntervalInSeconds"] = value["interval_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeBufferingHints:
    out: SnowflakeBufferingHints = {}  # type: ignore[typeddict-item]
    if "SizeInMBs" in data:
        out["size_in_m_bs"] = data["SizeInMBs"]
    if "IntervalInSeconds" in data:
        out["interval_in_seconds"] = data["IntervalInSeconds"]
    return out
