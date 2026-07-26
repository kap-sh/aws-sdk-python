"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ParseJSON``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.destination_field
    import capo_cloudwatch_logs.types.source


class ParseJSON(TypedDict, closed=True):
    source: NotRequired["capo_cloudwatch_logs.types.source.Source"]
    """<p>Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, <code>store.book</code> </p>"""
    destination: NotRequired[
        "capo_cloudwatch_logs.types.destination_field.DestinationField"
    ]
    """<p>The location to put the parsed key value pair into. If you omit this parameter, it is placed under the root node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParseJSON) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    if "destination" in value:
        out["destination"] = value["destination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParseJSON:
    out: ParseJSON = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    if "destination" in data:
        out["destination"] = data["destination"]
    return out
