"""Generated from Smithy shape ``com.amazonaws.pinpoint#ResultRowValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class ResultRowValue(TypedDict, closed=True):
    key: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The friendly name of the metric whose value is specified by the Value property.</p>"""
    type: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The data type of the value specified by the Value property.</p>"""
    value: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>In a Values object, the value for the metric that the query retrieved data for. In a GroupedBys object, the value for the field that was used to group data in a result set that contains multiple results (Values objects).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResultRowValue) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "type" in value:
        out["Type"] = value["type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ResultRowValue:
    out: ResultRowValue = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
