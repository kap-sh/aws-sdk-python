"""Generated from Smithy shape ``com.amazonaws.devopsguru#PerformanceInsightsReferenceComparisonValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.performance_insights_reference_metric
    import capo_devops_guru.types.performance_insights_reference_scalar


class PerformanceInsightsReferenceComparisonValues(TypedDict, closed=True):
    reference_scalar: NotRequired[
        "capo_devops_guru.types.performance_insights_reference_scalar.PerformanceInsightsReferenceScalar"
    ]
    """<p>A scalar value DevOps Guru for a metric that DevOps Guru compares to actual metric values. This reference value is used to determine if an actual metric value should be considered anomalous.</p>"""
    reference_metric: NotRequired[
        "capo_devops_guru.types.performance_insights_reference_metric.PerformanceInsightsReferenceMetric"
    ]
    """<p>A metric that DevOps Guru compares to actual metric values. This reference metric is used to determine if an actual metric should be considered anomalous.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceInsightsReferenceComparisonValues) -> dict:
    out: dict = {}
    if "reference_scalar" in value:
        import capo_devops_guru.types.performance_insights_reference_scalar

        out["ReferenceScalar"] = (
            capo_devops_guru.types.performance_insights_reference_scalar.serialize_json(
                value["reference_scalar"]
            )
        )
    if "reference_metric" in value:
        import capo_devops_guru.types.performance_insights_reference_metric

        out["ReferenceMetric"] = (
            capo_devops_guru.types.performance_insights_reference_metric.serialize_json(
                value["reference_metric"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerformanceInsightsReferenceComparisonValues:
    out: PerformanceInsightsReferenceComparisonValues = {}  # type: ignore[typeddict-item]
    if "ReferenceScalar" in data:
        import capo_devops_guru.types.performance_insights_reference_scalar

        out["reference_scalar"] = (
            capo_devops_guru.types.performance_insights_reference_scalar.deserialize_json(
                data["ReferenceScalar"]
            )
        )
    if "ReferenceMetric" in data:
        import capo_devops_guru.types.performance_insights_reference_metric

        out["reference_metric"] = (
            capo_devops_guru.types.performance_insights_reference_metric.deserialize_json(
                data["ReferenceMetric"]
            )
        )
    return out
