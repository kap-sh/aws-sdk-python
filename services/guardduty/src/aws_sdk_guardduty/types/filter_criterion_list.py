"""Generated from Smithy shape ``com.amazonaws.guardduty#FilterCriterionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.filter_criterion

FilterCriterionList: TypeAlias = list[
    "aws_sdk_guardduty.types.filter_criterion.FilterCriterion"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterCriterionList) -> list:
    import aws_sdk_guardduty.types.filter_criterion

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.filter_criterion.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterCriterionList:
    import aws_sdk_guardduty.types.filter_criterion

    out: FilterCriterionList = []
    for item in data:
        out.append(aws_sdk_guardduty.types.filter_criterion.deserialize_json(item))
    return out
