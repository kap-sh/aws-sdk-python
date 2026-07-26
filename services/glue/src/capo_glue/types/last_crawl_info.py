"""Generated from Smithy shape ``com.amazonaws.glue#LastCrawlInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.last_crawl_status
    import capo_glue.types.log_group
    import capo_glue.types.log_stream
    import capo_glue.types.message_prefix
    import capo_glue.types.timestamp


class LastCrawlInfo(TypedDict, closed=True):
    status: NotRequired["capo_glue.types.last_crawl_status.LastCrawlStatus"]
    """<p>Status of the last crawl.</p>"""
    error_message: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>If an error occurred, the error information about the last crawl.</p>"""
    log_group: NotRequired["capo_glue.types.log_group.LogGroup"]
    """<p>The log group for the last crawl.</p>"""
    log_stream: NotRequired["capo_glue.types.log_stream.LogStream"]
    """<p>The log stream for the last crawl.</p>"""
    message_prefix: NotRequired["capo_glue.types.message_prefix.MessagePrefix"]
    """<p>The prefix for a message about this crawl.</p>"""
    start_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the crawl started.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastCrawlInfo) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_glue.types.last_crawl_status

        out["Status"] = capo_glue.types.last_crawl_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
    if "log_stream" in value:
        out["LogStream"] = value["log_stream"]
    if "message_prefix" in value:
        out["MessagePrefix"] = value["message_prefix"]
    if "start_time" in value:
        import capo_glue.types.timestamp

        out["StartTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LastCrawlInfo:
    out: LastCrawlInfo = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_glue.types.last_crawl_status

        out["status"] = capo_glue.types.last_crawl_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "LogGroup" in data:
        out["log_group"] = data["LogGroup"]
    if "LogStream" in data:
        out["log_stream"] = data["LogStream"]
    if "MessagePrefix" in data:
        out["message_prefix"] = data["MessagePrefix"]
    if "StartTime" in data:
        import capo_glue.types.timestamp

        out["start_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    return out
