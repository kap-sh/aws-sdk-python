"""Generated from Smithy shape ``com.amazonaws.guardduty#FilterCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.long_value
    import aws_sdk_guardduty.types.non_empty_string


class FilterCondition(TypedDict):
    equals_value: NotRequired["aws_sdk_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>Represents an <i>equal</i> <b/> condition to be applied to a single field when querying for scan entries.</p>"""
    greater_than: NotRequired["aws_sdk_guardduty.types.long_value.LongValue"]
    """<p>Represents a <i>greater than</i> condition to be applied to a single field when querying for scan entries.</p>"""
    less_than: NotRequired["aws_sdk_guardduty.types.long_value.LongValue"]
    """<p>Represents a <i>less than</i> condition to be applied to a single field when querying for scan entries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCondition) -> dict:
    out: dict = {}
    if "equals_value" in value:
        out["equalsValue"] = value["equals_value"]
    if "greater_than" in value:
        out["greaterThan"] = value["greater_than"]
    if "less_than" in value:
        out["lessThan"] = value["less_than"]
    return out


def deserialize_json(data: dict) -> FilterCondition:
    out: FilterCondition = {}  # type: ignore[typeddict-item]
    if "equalsValue" in data:
        out["equals_value"] = data["equalsValue"]
    if "greaterThan" in data:
        out["greater_than"] = data["greaterThan"]
    if "lessThan" in data:
        out["less_than"] = data["lessThan"]
    return out
