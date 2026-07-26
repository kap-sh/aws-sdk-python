"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LogGroupField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.field
    import capo_cloudwatch_logs.types.percentage


class LogGroupField(TypedDict, closed=True):
    name: NotRequired["capo_cloudwatch_logs.types.field.Field"]
    """<p>The name of a log field.</p>"""
    percent: "capo_cloudwatch_logs.types.percentage.Percentage"
    """<p>The percentage of log events queried that contained the field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogGroupField) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["percent"] = value.get("percent", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> LogGroupField:
    out: LogGroupField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "percent" in data:
        out["percent"] = data["percent"]
    else:
        out["percent"] = 0
    return out
