"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Grok``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.grok_match
    import aws_sdk_cloudwatch_logs.types.source


class Grok(TypedDict):
    source: NotRequired["aws_sdk_cloudwatch_logs.types.source.Source"]
    """<p>The path to the field in the log event that you want to parse. If you omit this value, the whole log message is parsed.</p>"""
    match: "aws_sdk_cloudwatch_logs.types.grok_match.GrokMatch"
    """<p>The grok pattern to match against the log event. For a list of supported grok patterns, see <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Configurable.html#CloudWatch-Logs-Transformation-Grok\">Supported grok patterns</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Grok) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    out["match"] = value["match"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Grok:
    out: Grok = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    if "match" in data:
        out["match"] = data["match"]
    else:
        raise DeserializationError("Grok.match required")
    return out
