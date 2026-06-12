"""Generated from Smithy shape ``com.amazonaws.costexplorer#RightsizingRecommendationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class RightsizingRecommendationSummary(TypedDict):
    total_recommendation_count: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The total number of instance recommendations.</p>"""
    estimated_total_monthly_savings_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The estimated total savings resulting from modifications, on a monthly basis.</p>"""
    savings_currency_code: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The currency code that Amazon Web Services used to calculate the savings.</p>"""
    savings_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p> The savings percentage based on the recommended modifications. It's relative to the total On-Demand costs that are associated with these instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RightsizingRecommendationSummary) -> dict:
    out: dict = {}
    if "total_recommendation_count" in value:
        out["TotalRecommendationCount"] = value["total_recommendation_count"]
    if "estimated_total_monthly_savings_amount" in value:
        out["EstimatedTotalMonthlySavingsAmount"] = value[
            "estimated_total_monthly_savings_amount"
        ]
    if "savings_currency_code" in value:
        out["SavingsCurrencyCode"] = value["savings_currency_code"]
    if "savings_percentage" in value:
        out["SavingsPercentage"] = value["savings_percentage"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RightsizingRecommendationSummary:
    out: RightsizingRecommendationSummary = {}  # type: ignore[typeddict-item]
    if "TotalRecommendationCount" in data:
        out["total_recommendation_count"] = data["TotalRecommendationCount"]
    if "EstimatedTotalMonthlySavingsAmount" in data:
        out["estimated_total_monthly_savings_amount"] = data[
            "EstimatedTotalMonthlySavingsAmount"
        ]
    if "SavingsCurrencyCode" in data:
        out["savings_currency_code"] = data["SavingsCurrencyCode"]
    if "SavingsPercentage" in data:
        out["savings_percentage"] = data["SavingsPercentage"]
    return out
