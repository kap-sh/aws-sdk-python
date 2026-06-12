"""Generated from Smithy shape ``com.amazonaws.costexplorer#TerminateRecommendationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class TerminateRecommendationDetail(TypedDict):
    estimated_monthly_savings: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated savings that result from modification, on a monthly basis.</p>"""
    currency_code: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The currency code that Amazon Web Services used to calculate the costs for this instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateRecommendationDetail) -> dict:
    out: dict = {}
    if "estimated_monthly_savings" in value:
        out["EstimatedMonthlySavings"] = value["estimated_monthly_savings"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateRecommendationDetail:
    out: TerminateRecommendationDetail = {}  # type: ignore[typeddict-item]
    if "EstimatedMonthlySavings" in data:
        out["estimated_monthly_savings"] = data["EstimatedMonthlySavings"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    return out
