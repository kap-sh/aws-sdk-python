"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResultField``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.field
    import aws_sdk_cloudwatch_logs.types.value


class ResultField(TypedDict):
    field: NotRequired["aws_sdk_cloudwatch_logs.types.field.Field"]
    """<p>The log event field.</p>"""
    value: NotRequired["aws_sdk_cloudwatch_logs.types.value.Value"]
    """<p>The value of this field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResultField) -> dict:
    out: dict = {}
    if "field" in value:
        out["field"] = value["field"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResultField:
    out: ResultField = {}  # type: ignore[typeddict-item]
    if "field" in data:
        out["field"] = data["field"]
    if "value" in data:
        out["value"] = data["value"]
    return out
