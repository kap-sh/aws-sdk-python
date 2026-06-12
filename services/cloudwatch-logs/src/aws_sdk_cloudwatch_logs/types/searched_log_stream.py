"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#SearchedLogStream``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_stream_name
    import aws_sdk_cloudwatch_logs.types.log_stream_searched_completely


class SearchedLogStream(TypedDict):
    log_stream_name: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_stream_name.LogStreamName"
    ]
    """<p>The name of the log stream.</p>"""
    searched_completely: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_stream_searched_completely.LogStreamSearchedCompletely"
    ]
    """<p>Indicates whether all the events in this log stream were searched.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchedLogStream) -> dict:
    out: dict = {}
    if "log_stream_name" in value:
        out["logStreamName"] = value["log_stream_name"]
    if "searched_completely" in value:
        out["searchedCompletely"] = value["searched_completely"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchedLogStream:
    out: SearchedLogStream = {}  # type: ignore[typeddict-item]
    if "logStreamName" in data:
        out["log_stream_name"] = data["logStreamName"]
    if "searchedCompletely" in data:
        out["searched_completely"] = data["searchedCompletely"]
    return out
