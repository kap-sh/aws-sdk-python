"""Generated from Smithy shape ``com.amazonaws.guardduty#FilterCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.filter_criterion_list


class FilterCriteria(TypedDict):
    filter_criterion: NotRequired[
        "aws_sdk_guardduty.types.filter_criterion_list.FilterCriterionList"
    ]
    """<p>Represents a condition that when matched will be added to the response of the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriteria) -> dict:
    out: dict = {}
    if "filter_criterion" in value:
        import aws_sdk_guardduty.types.filter_criterion_list

        out["filterCriterion"] = (
            aws_sdk_guardduty.types.filter_criterion_list.serialize_json(
                value["filter_criterion"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterCriteria:
    out: FilterCriteria = {}  # type: ignore[typeddict-item]
    if "filterCriterion" in data:
        import aws_sdk_guardduty.types.filter_criterion_list

        out["filter_criterion"] = (
            aws_sdk_guardduty.types.filter_criterion_list.deserialize_json(
                data["filterCriterion"]
            )
        )
    return out
