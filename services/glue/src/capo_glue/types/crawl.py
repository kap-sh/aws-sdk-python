"""Generated from Smithy shape ``com.amazonaws.glue#Crawl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.crawl_state
    import capo_glue.types.description_string
    import capo_glue.types.log_group
    import capo_glue.types.log_stream
    import capo_glue.types.timestamp_value


class Crawl(TypedDict, closed=True):
    state: NotRequired["capo_glue.types.crawl_state.CrawlState"]
    """<p>The state of the crawler.</p>"""
    started_on: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time on which the crawl started.</p>"""
    completed_on: NotRequired["capo_glue.types.timestamp_value.TimestampValue"]
    """<p>The date and time on which the crawl completed.</p>"""
    error_message: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>The error message associated with the crawl.</p>"""
    log_group: NotRequired["capo_glue.types.log_group.LogGroup"]
    """<p>The log group associated with the crawl.</p>"""
    log_stream: NotRequired["capo_glue.types.log_stream.LogStream"]
    """<p>The log stream associated with the crawl.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Crawl) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_glue.types.crawl_state

        out["State"] = capo_glue.types.crawl_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "started_on" in value:
        import capo_glue.types.timestamp_value

        out["StartedOn"] = capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "completed_on" in value:
        import capo_glue.types.timestamp_value

        out["CompletedOn"] = capo_glue.types.timestamp_value.serialize_aws_json_1_1(
            value["completed_on"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
    if "log_stream" in value:
        out["LogStream"] = value["log_stream"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Crawl:
    out: Crawl = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import capo_glue.types.crawl_state

        out["state"] = capo_glue.types.crawl_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if "StartedOn" in data:
        import capo_glue.types.timestamp_value

        out["started_on"] = capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if "CompletedOn" in data:
        import capo_glue.types.timestamp_value

        out["completed_on"] = capo_glue.types.timestamp_value.deserialize_aws_json_1_1(
            data["CompletedOn"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "LogGroup" in data:
        out["log_group"] = data["LogGroup"]
    if "LogStream" in data:
        out["log_stream"] = data["LogStream"]
    return out
