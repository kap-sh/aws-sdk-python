"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ParseVPC``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.source


class ParseVPC(TypedDict, closed=True):
    source: NotRequired["capo_cloudwatch_logs.types.source.Source"]
    """<p>Omit this parameter and the whole log message will be processed by this processor. No other value than <code>@message</code> is allowed for <code>source</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParseVPC) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParseVPC:
    out: ParseVPC = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    return out
