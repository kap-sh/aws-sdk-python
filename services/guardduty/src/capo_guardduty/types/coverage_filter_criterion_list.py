"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageFilterCriterionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.coverage_filter_criterion

CoverageFilterCriterionList: TypeAlias = list[
    "capo_guardduty.types.coverage_filter_criterion.CoverageFilterCriterion"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoverageFilterCriterionList) -> list:
    import capo_guardduty.types.coverage_filter_criterion

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.coverage_filter_criterion.serialize_json(item))
    return out


def deserialize_json(data: list) -> CoverageFilterCriterionList:
    import capo_guardduty.types.coverage_filter_criterion

    out: CoverageFilterCriterionList = []
    for item in data:
        out.append(
            capo_guardduty.types.coverage_filter_criterion.deserialize_json(item)
        )
    return out
