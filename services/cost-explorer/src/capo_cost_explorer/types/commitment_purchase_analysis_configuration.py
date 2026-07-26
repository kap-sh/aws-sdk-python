"""Generated from Smithy shape ``com.amazonaws.costexplorer#CommitmentPurchaseAnalysisConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.savings_plans_purchase_analysis_configuration


class CommitmentPurchaseAnalysisConfiguration(TypedDict, closed=True):
    savings_plans_purchase_analysis_configuration: NotRequired[
        "capo_cost_explorer.types.savings_plans_purchase_analysis_configuration.SavingsPlansPurchaseAnalysisConfiguration"
    ]
    """<p>The configuration for the Savings Plans purchase analysis.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommitmentPurchaseAnalysisConfiguration) -> dict:
    out: dict = {}
    if "savings_plans_purchase_analysis_configuration" in value:
        import capo_cost_explorer.types.savings_plans_purchase_analysis_configuration

        out["SavingsPlansPurchaseAnalysisConfiguration"] = (
            capo_cost_explorer.types.savings_plans_purchase_analysis_configuration.serialize_aws_json_1_1(
                value["savings_plans_purchase_analysis_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CommitmentPurchaseAnalysisConfiguration:
    out: CommitmentPurchaseAnalysisConfiguration = {}  # type: ignore[typeddict-item]
    if "SavingsPlansPurchaseAnalysisConfiguration" in data:
        import capo_cost_explorer.types.savings_plans_purchase_analysis_configuration

        out["savings_plans_purchase_analysis_configuration"] = (
            capo_cost_explorer.types.savings_plans_purchase_analysis_configuration.deserialize_aws_json_1_1(
                data["SavingsPlansPurchaseAnalysisConfiguration"]
            )
        )
    return out
