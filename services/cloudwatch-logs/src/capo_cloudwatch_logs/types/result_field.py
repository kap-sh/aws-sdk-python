"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ResultField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.field
    import capo_cloudwatch_logs.types.value


class ResultField(TypedDict, closed=True):
    field: NotRequired["capo_cloudwatch_logs.types.field.Field"]
    """<p>The log event field.</p>"""
    value: NotRequired["capo_cloudwatch_logs.types.value.Value"]
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
    if data.get("field") is not None:
        out["field"] = data["field"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
