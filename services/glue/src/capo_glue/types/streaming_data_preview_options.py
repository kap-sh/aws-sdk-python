"""Generated from Smithy shape ``com.amazonaws.glue#StreamingDataPreviewOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.polling_time
    import capo_glue.types.positive_long


class StreamingDataPreviewOptions(TypedDict, closed=True):
    polling_time: NotRequired["capo_glue.types.polling_time.PollingTime"]
    """<p>The polling time in milliseconds.</p>"""
    record_polling_limit: NotRequired["capo_glue.types.positive_long.PositiveLong"]
    """<p>The limit to the number of records polled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StreamingDataPreviewOptions) -> dict:
    out: dict = {}
    if "polling_time" in value:
        out["PollingTime"] = value["polling_time"]
    if "record_polling_limit" in value:
        out["RecordPollingLimit"] = value["record_polling_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StreamingDataPreviewOptions:
    out: StreamingDataPreviewOptions = {}  # type: ignore[typeddict-item]
    if "PollingTime" in data:
        out["polling_time"] = data["PollingTime"]
    if "RecordPollingLimit" in data:
        out["record_polling_limit"] = data["RecordPollingLimit"]
    return out
