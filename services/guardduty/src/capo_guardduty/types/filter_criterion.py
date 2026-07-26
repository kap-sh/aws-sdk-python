"""Generated from Smithy shape ``com.amazonaws.guardduty#FilterCriterion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.criterion_key
    import capo_guardduty.types.filter_condition


class FilterCriterion(TypedDict, closed=True):
    criterion_key: NotRequired["capo_guardduty.types.criterion_key.CriterionKey"]
    """<p>An enum value representing possible scan properties to match with given scan entries.</p>"""
    filter_condition: NotRequired[
        "capo_guardduty.types.filter_condition.FilterCondition"
    ]
    """<p>Contains information about the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriterion) -> dict:
    out: dict = {}
    if "criterion_key" in value:
        import capo_guardduty.types.criterion_key

        out["criterionKey"] = capo_guardduty.types.criterion_key.serialize_json(
            value["criterion_key"]
        )
    if "filter_condition" in value:
        import capo_guardduty.types.filter_condition

        out["filterCondition"] = capo_guardduty.types.filter_condition.serialize_json(
            value["filter_condition"]
        )
    return out


def deserialize_json(data: dict) -> FilterCriterion:
    out: FilterCriterion = {}  # type: ignore[typeddict-item]
    if "criterionKey" in data:
        import capo_guardduty.types.criterion_key

        out["criterion_key"] = capo_guardduty.types.criterion_key.deserialize_json(
            data["criterionKey"]
        )
    if "filterCondition" in data:
        import capo_guardduty.types.filter_condition

        out["filter_condition"] = (
            capo_guardduty.types.filter_condition.deserialize_json(
                data["filterCondition"]
            )
        )
    return out
