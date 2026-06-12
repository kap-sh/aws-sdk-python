"""Generated from Smithy shape ``com.amazonaws.glue#CrawlerHistory``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.crawl_id
    import aws_sdk_glue.types.crawler_history_state
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.log_group
    import aws_sdk_glue.types.log_stream
    import aws_sdk_glue.types.message_prefix
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.non_negative_double
    import aws_sdk_glue.types.timestamp


class CrawlerHistory(TypedDict):
    crawl_id: NotRequired["aws_sdk_glue.types.crawl_id.CrawlId"]
    """<p>A UUID identifier for each crawl.</p>"""
    state: NotRequired["aws_sdk_glue.types.crawler_history_state.CrawlerHistoryState"]
    """<p>The state of the crawl.</p>"""
    start_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time on which the crawl started.</p>"""
    end_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time on which the crawl ended.</p>"""
    summary: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>A run summary for the specific crawl in JSON. Contains the catalog tables and partitions that were added, updated, or deleted.</p>"""
    error_message: NotRequired[
        "aws_sdk_glue.types.description_string.DescriptionString"
    ]
    """<p>If an error occurred, the error message associated with the crawl.</p>"""
    log_group: NotRequired["aws_sdk_glue.types.log_group.LogGroup"]
    """<p>The log group associated with the crawl.</p>"""
    log_stream: NotRequired["aws_sdk_glue.types.log_stream.LogStream"]
    """<p>The log stream associated with the crawl.</p>"""
    message_prefix: NotRequired["aws_sdk_glue.types.message_prefix.MessagePrefix"]
    """<p>The prefix for a CloudWatch message about this crawl.</p>"""
    dpu_hour: "aws_sdk_glue.types.non_negative_double.NonNegativeDouble"
    """<p>The number of data processing units (DPU) used in hours for the crawl.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CrawlerHistory) -> dict:
    out: dict = {}
    if "crawl_id" in value:
        out["CrawlId"] = value["crawl_id"]
    if "state" in value:
        import aws_sdk_glue.types.crawler_history_state

        out["State"] = aws_sdk_glue.types.crawler_history_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "start_time" in value:
        import aws_sdk_glue.types.timestamp

        out["StartTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_glue.types.timestamp

        out["EndTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "summary" in value:
        out["Summary"] = value["summary"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
    if "log_stream" in value:
        out["LogStream"] = value["log_stream"]
    if "message_prefix" in value:
        out["MessagePrefix"] = value["message_prefix"]
    out["DPUHour"] = value.get("dpu_hour", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CrawlerHistory:
    out: CrawlerHistory = {}  # type: ignore[typeddict-item]
    if "CrawlId" in data:
        out["crawl_id"] = data["CrawlId"]
    if "State" in data:
        import aws_sdk_glue.types.crawler_history_state

        out["state"] = (
            aws_sdk_glue.types.crawler_history_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_glue.types.timestamp

        out["start_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_glue.types.timestamp

        out["end_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "Summary" in data:
        out["summary"] = data["Summary"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "LogGroup" in data:
        out["log_group"] = data["LogGroup"]
    if "LogStream" in data:
        out["log_stream"] = data["LogStream"]
    if "MessagePrefix" in data:
        out["message_prefix"] = data["MessagePrefix"]
    if "DPUHour" in data:
        out["dpu_hour"] = data["DPUHour"]
    else:
        out["dpu_hour"] = 0
    return out
