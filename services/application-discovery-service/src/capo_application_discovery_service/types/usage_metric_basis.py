"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#UsageMetricBasis``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.usage_metric_basis_name
    import capo_application_discovery_service.types.usage_metric_percentage_adjust


class UsageMetricBasis(TypedDict, closed=True):
    name: NotRequired[
        "capo_application_discovery_service.types.usage_metric_basis_name.UsageMetricBasisName"
    ]
    """<p> A utilization metric that is used by the recommendations. </p>"""
    percentage_adjust: NotRequired[
        "capo_application_discovery_service.types.usage_metric_percentage_adjust.UsageMetricPercentageAdjust"
    ]
    """<p> Specifies the percentage of the specified utilization metric that is used by the recommendations. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageMetricBasis) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "percentage_adjust" in value:
        out["percentageAdjust"] = value["percentage_adjust"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UsageMetricBasis:
    out: UsageMetricBasis = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "percentageAdjust" in data:
        out["percentage_adjust"] = data["percentageAdjust"]
    return out
