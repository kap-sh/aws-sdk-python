"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QueryStatus``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.double
    import aws_sdk_timestream_query.types.long


class QueryStatus(TypedDict):
    progress_percentage: "aws_sdk_timestream_query.types.double.Double"
    """<p>The progress of the query, expressed as a percentage.</p>"""
    cumulative_bytes_scanned: "aws_sdk_timestream_query.types.long.Long"
    """<p>The amount of data scanned by the query in bytes. This is a cumulative sum and represents the total amount of bytes scanned since the query was started. </p>"""
    cumulative_bytes_metered: "aws_sdk_timestream_query.types.long.Long"
    """<p>The amount of data scanned by the query in bytes that you will be charged for. This is a cumulative sum and represents the total amount of data that you will be charged for since the query was started. The charge is applied only once and is either applied when the query completes running or when the query is cancelled. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryStatus) -> dict:
    out: dict = {}
    out["ProgressPercentage"] = value.get("progress_percentage", 0)
    out["CumulativeBytesScanned"] = value.get("cumulative_bytes_scanned", 0)
    out["CumulativeBytesMetered"] = value.get("cumulative_bytes_metered", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryStatus:
    out: QueryStatus = {}  # type: ignore[typeddict-item]
    if "ProgressPercentage" in data:
        out["progress_percentage"] = data["ProgressPercentage"]
    else:
        out["progress_percentage"] = 0
    if "CumulativeBytesScanned" in data:
        out["cumulative_bytes_scanned"] = data["CumulativeBytesScanned"]
    else:
        out["cumulative_bytes_scanned"] = 0
    if "CumulativeBytesMetered" in data:
        out["cumulative_bytes_metered"] = data["CumulativeBytesMetered"]
    else:
        out["cumulative_bytes_metered"] = 0
    return out
