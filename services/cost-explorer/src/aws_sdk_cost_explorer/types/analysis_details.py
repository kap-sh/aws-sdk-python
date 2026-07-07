"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnalysisDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.savings_plans_purchase_analysis_details


class AnalysisDetails(TypedDict, closed=True):
    savings_plans_purchase_analysis_details: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_purchase_analysis_details.SavingsPlansPurchaseAnalysisDetails"
    ]
    """<p>Details about the Savings Plans purchase analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalysisDetails) -> dict:
    out: dict = {}
    if "savings_plans_purchase_analysis_details" in value:
        import aws_sdk_cost_explorer.types.savings_plans_purchase_analysis_details

        out["SavingsPlansPurchaseAnalysisDetails"] = (
            aws_sdk_cost_explorer.types.savings_plans_purchase_analysis_details.serialize_aws_json_1_1(
                value["savings_plans_purchase_analysis_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalysisDetails:
    out: AnalysisDetails = {}  # type: ignore[typeddict-item]
    if "SavingsPlansPurchaseAnalysisDetails" in data:
        import aws_sdk_cost_explorer.types.savings_plans_purchase_analysis_details

        out["savings_plans_purchase_analysis_details"] = (
            aws_sdk_cost_explorer.types.savings_plans_purchase_analysis_details.deserialize_aws_json_1_1(
                data["SavingsPlansPurchaseAnalysisDetails"]
            )
        )
    return out
