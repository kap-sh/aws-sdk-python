"""Generated from Smithy shape ``com.amazonaws.guardduty#FilterCriterionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.filter_criterion

FilterCriterionList: TypeAlias = list[
    "capo_guardduty.types.filter_criterion.FilterCriterion"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriterionList) -> list:
    import capo_guardduty.types.filter_criterion

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.filter_criterion.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterCriterionList:
    import capo_guardduty.types.filter_criterion

    out: FilterCriterionList = []
    for item in data:
        out.append(capo_guardduty.types.filter_criterion.deserialize_json(item))
    return out
