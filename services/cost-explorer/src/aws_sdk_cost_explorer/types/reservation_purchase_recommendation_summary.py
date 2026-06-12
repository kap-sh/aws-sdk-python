"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationPurchaseRecommendationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.generic_string


class ReservationPurchaseRecommendationSummary(TypedDict):
    total_estimated_monthly_savings_amount: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The total amount that Amazon Web Services estimates that this recommendation could save you in a month.</p>"""
    total_estimated_monthly_savings_percentage: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The total amount that Amazon Web Services estimates that this recommendation could save you in a month, as a percentage of your costs.</p>"""
    currency_code: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The currency code used for this recommendation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationPurchaseRecommendationSummary) -> dict:
    out: dict = {}
    if "total_estimated_monthly_savings_amount" in value:
        out["TotalEstimatedMonthlySavingsAmount"] = value[
            "total_estimated_monthly_savings_amount"
        ]
    if "total_estimated_monthly_savings_percentage" in value:
        out["TotalEstimatedMonthlySavingsPercentage"] = value[
            "total_estimated_monthly_savings_percentage"
        ]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservationPurchaseRecommendationSummary:
    out: ReservationPurchaseRecommendationSummary = {}  # type: ignore[typeddict-item]
    if "TotalEstimatedMonthlySavingsAmount" in data:
        out["total_estimated_monthly_savings_amount"] = data[
            "TotalEstimatedMonthlySavingsAmount"
        ]
    if "TotalEstimatedMonthlySavingsPercentage" in data:
        out["total_estimated_monthly_savings_percentage"] = data[
            "TotalEstimatedMonthlySavingsPercentage"
        ]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    return out
