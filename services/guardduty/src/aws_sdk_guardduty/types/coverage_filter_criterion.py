"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageFilterCriterion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_filter_condition
    import aws_sdk_guardduty.types.coverage_filter_criterion_key


class CoverageFilterCriterion(TypedDict, closed=True):
    criterion_key: NotRequired[
        "aws_sdk_guardduty.types.coverage_filter_criterion_key.CoverageFilterCriterionKey"
    ]
    """<p>An enum value representing possible filter fields.</p> <note> <p>Replace the enum value <code>CLUSTER_NAME</code> with <code>EKS_CLUSTER_NAME</code>. <code>CLUSTER_NAME</code> has been deprecated.</p> </note>"""
    filter_condition: NotRequired[
        "aws_sdk_guardduty.types.coverage_filter_condition.CoverageFilterCondition"
    ]
    """<p>Contains information about the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageFilterCriterion) -> dict:
    out: dict = {}
    if "criterion_key" in value:
        import aws_sdk_guardduty.types.coverage_filter_criterion_key

        out["criterionKey"] = (
            aws_sdk_guardduty.types.coverage_filter_criterion_key.serialize_json(
                value["criterion_key"]
            )
        )
    if "filter_condition" in value:
        import aws_sdk_guardduty.types.coverage_filter_condition

        out["filterCondition"] = (
            aws_sdk_guardduty.types.coverage_filter_condition.serialize_json(
                value["filter_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoverageFilterCriterion:
    out: CoverageFilterCriterion = {}  # type: ignore[typeddict-item]
    if "criterionKey" in data:
        import aws_sdk_guardduty.types.coverage_filter_criterion_key

        out["criterion_key"] = (
            aws_sdk_guardduty.types.coverage_filter_criterion_key.deserialize_json(
                data["criterionKey"]
            )
        )
    if "filterCondition" in data:
        import aws_sdk_guardduty.types.coverage_filter_condition

        out["filter_condition"] = (
            aws_sdk_guardduty.types.coverage_filter_condition.deserialize_json(
                data["filterCondition"]
            )
        )
    return out
