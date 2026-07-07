"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_filter_criterion_list


class CoverageFilterCriteria(TypedDict, closed=True):
    filter_criterion: NotRequired[
        "aws_sdk_guardduty.types.coverage_filter_criterion_list.CoverageFilterCriterionList"
    ]
    """<p>Represents a condition that when matched will be added to the response of the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageFilterCriteria) -> dict:
    out: dict = {}
    if "filter_criterion" in value:
        import aws_sdk_guardduty.types.coverage_filter_criterion_list

        out["filterCriterion"] = (
            aws_sdk_guardduty.types.coverage_filter_criterion_list.serialize_json(
                value["filter_criterion"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoverageFilterCriteria:
    out: CoverageFilterCriteria = {}  # type: ignore[typeddict-item]
    if "filterCriterion" in data:
        import aws_sdk_guardduty.types.coverage_filter_criterion_list

        out["filter_criterion"] = (
            aws_sdk_guardduty.types.coverage_filter_criterion_list.deserialize_json(
                data["filterCriterion"]
            )
        )
    return out
