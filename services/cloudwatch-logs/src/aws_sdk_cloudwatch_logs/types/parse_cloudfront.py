"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ParseCloudfront``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.source


class ParseCloudfront(TypedDict):
    source: NotRequired["aws_sdk_cloudwatch_logs.types.source.Source"]
    """<p>Omit this parameter and the whole log message will be processed by this processor. No other value than <code>@message</code> is allowed for <code>source</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParseCloudfront) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParseCloudfront:
    out: ParseCloudfront = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    return out
