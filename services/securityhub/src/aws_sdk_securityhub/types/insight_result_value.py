"""Generated from Smithy shape ``com.amazonaws.securityhub#InsightResultValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class InsightResultValue(TypedDict):
    group_by_attribute_value: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The value of the attribute that the findings are grouped by for the insight whose results are returned by the <code>GetInsightResults</code> operation.</p>"""
    count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of findings returned for each <code>GroupByAttributeValue</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightResultValue) -> dict:
    out: dict = {}
    if "group_by_attribute_value" in value:
        out["GroupByAttributeValue"] = value["group_by_attribute_value"]
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_json(data: dict) -> InsightResultValue:
    out: InsightResultValue = {}  # type: ignore[typeddict-item]
    if "GroupByAttributeValue" in data:
        out["group_by_attribute_value"] = data["GroupByAttributeValue"]
    if "Count" in data:
        out["count"] = data["Count"]
    return out
