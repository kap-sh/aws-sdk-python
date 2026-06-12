"""Generated from Smithy shape ``com.amazonaws.securityhub#GroupByValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class GroupByValue(TypedDict):
    field_value: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The value of the field by which findings are grouped.</p>"""
    count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings for a specific <code>FieldValue</code> and <code>GroupByField</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupByValue) -> dict:
    out: dict = {}
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_json(data: dict) -> GroupByValue:
    out: GroupByValue = {}  # type: ignore[typeddict-item]
    if "FieldValue" in data:
        out["field_value"] = data["FieldValue"]
    if "Count" in data:
        out["count"] = data["Count"]
    return out
