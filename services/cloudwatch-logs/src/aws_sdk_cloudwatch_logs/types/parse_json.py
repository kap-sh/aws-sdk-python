"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ParseJSON``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.destination_field
    import aws_sdk_cloudwatch_logs.types.source


class ParseJSON(TypedDict):
    source: NotRequired["aws_sdk_cloudwatch_logs.types.source.Source"]
    """<p>Path to the field in the log event that will be parsed. Use dot notation to access child fields. For example, <code>store.book</code> </p>"""
    destination: NotRequired[
        "aws_sdk_cloudwatch_logs.types.destination_field.DestinationField"
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
