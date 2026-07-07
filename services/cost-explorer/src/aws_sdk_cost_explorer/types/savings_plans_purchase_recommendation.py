"""Generated from Smithy shape ``com.amazonaws.costexplorer#SavingsPlansPurchaseRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.account_scope
    import aws_sdk_cost_explorer.types.lookback_period_in_days
    import aws_sdk_cost_explorer.types.payment_option
    import aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_detail_list
    import aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_summary
    import aws_sdk_cost_explorer.types.supported_savings_plans_type
    import aws_sdk_cost_explorer.types.term_in_years


class SavingsPlansPurchaseRecommendation(TypedDict, closed=True):
    account_scope: NotRequired["aws_sdk_cost_explorer.types.account_scope.AccountScope"]
    """<p>The account scope that you want your recommendations for. Amazon Web Services calculates recommendations that include the management account and member accounts if the value is set to <code>PAYER</code>. If the value is <code>LINKED</code>, recommendations are calculated for individual member accounts only.</p>"""
    savings_plans_type: NotRequired[
        "aws_sdk_cost_explorer.types.supported_savings_plans_type.SupportedSavingsPlansType"
    ]
    """<p>The requested Savings Plans recommendation type.</p>"""
    term_in_years: NotRequired["aws_sdk_cost_explorer.types.term_in_years.TermInYears"]
    """<p>The Savings Plans recommendation term in years. It's used to generate the recommendation.</p>"""
    payment_option: NotRequired[
        "aws_sdk_cost_explorer.types.payment_option.PaymentOption"
    ]
    """<p>The payment option that's used to generate the recommendation.</p>"""
    lookback_period_in_days: NotRequired[
        "aws_sdk_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
    ]
    """<p>The lookback period in days that's used to generate the recommendation.</p>"""
    savings_plans_purchase_recommendation_details: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_detail_list.SavingsPlansPurchaseRecommendationDetailList"
    ]
    """<p>Details for the Savings Plans that we recommend that you purchase to cover existing Savings Plans eligible workloads.</p>"""
    savings_plans_purchase_recommendation_summary: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_summary.SavingsPlansPurchaseRecommendationSummary"
    ]
    """<p>Summary metrics for your Savings Plans Recommendations. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SavingsPlansPurchaseRecommendation) -> dict:
    out: dict = {}
    if "account_scope" in value:
        import aws_sdk_cost_explorer.types.account_scope

        out["AccountScope"] = (
            aws_sdk_cost_explorer.types.account_scope.serialize_aws_json_1_1(
                value["account_scope"]
            )
        )
    if "savings_plans_type" in value:
        import aws_sdk_cost_explorer.types.supported_savings_plans_type

        out["SavingsPlansType"] = (
            aws_sdk_cost_explorer.types.supported_savings_plans_type.serialize_aws_json_1_1(
                value["savings_plans_type"]
            )
        )
    if "term_in_years" in value:
        import aws_sdk_cost_explorer.types.term_in_years

        out["TermInYears"] = (
            aws_sdk_cost_explorer.types.term_in_years.serialize_aws_json_1_1(
                value["term_in_years"]
            )
        )
    if "payment_option" in value:
        import aws_sdk_cost_explorer.types.payment_option

        out["PaymentOption"] = (
            aws_sdk_cost_explorer.types.payment_option.serialize_aws_json_1_1(
                value["payment_option"]
            )
        )
    if "lookback_period_in_days" in value:
        import aws_sdk_cost_explorer.types.lookback_period_in_days

        out["LookbackPeriodInDays"] = (
            aws_sdk_cost_explorer.types.lookback_period_in_days.serialize_aws_json_1_1(
                value["lookback_period_in_days"]
            )
        )
    if "savings_plans_purchase_recommendation_details" in value:
        import aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_detail_list

        out["SavingsPlansPurchaseRecommendationDetails"] = (
            aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_detail_list.serialize_aws_json_1_1(
                value["savings_plans_purchase_recommendation_details"]
            )
        )
    if "savings_plans_purchase_recommendation_summary" in value:
        import aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_summary

        out["SavingsPlansPurchaseRecommendationSummary"] = (
            aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_summary.serialize_aws_json_1_1(
                value["savings_plans_purchase_recommendation_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SavingsPlansPurchaseRecommendation:
    out: SavingsPlansPurchaseRecommendation = {}  # type: ignore[typeddict-item]
    if "AccountScope" in data:
        import aws_sdk_cost_explorer.types.account_scope

        out["account_scope"] = (
            aws_sdk_cost_explorer.types.account_scope.deserialize_aws_json_1_1(
                data["AccountScope"]
            )
        )
    if "SavingsPlansType" in data:
        import aws_sdk_cost_explorer.types.supported_savings_plans_type

        out["savings_plans_type"] = (
            aws_sdk_cost_explorer.types.supported_savings_plans_type.deserialize_aws_json_1_1(
                data["SavingsPlansType"]
            )
        )
    if "TermInYears" in data:
        import aws_sdk_cost_explorer.types.term_in_years

        out["term_in_years"] = (
            aws_sdk_cost_explorer.types.term_in_years.deserialize_aws_json_1_1(
                data["TermInYears"]
            )
        )
    if "PaymentOption" in data:
        import aws_sdk_cost_explorer.types.payment_option

        out["payment_option"] = (
            aws_sdk_cost_explorer.types.payment_option.deserialize_aws_json_1_1(
                data["PaymentOption"]
            )
        )
    if "LookbackPeriodInDays" in data:
        import aws_sdk_cost_explorer.types.lookback_period_in_days

        out["lookback_period_in_days"] = (
            aws_sdk_cost_explorer.types.lookback_period_in_days.deserialize_aws_json_1_1(
                data["LookbackPeriodInDays"]
            )
        )
    if "SavingsPlansPurchaseRecommendationDetails" in data:
        import aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_detail_list

        out["savings_plans_purchase_recommendation_details"] = (
            aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_detail_list.deserialize_aws_json_1_1(
                data["SavingsPlansPurchaseRecommendationDetails"]
            )
        )
    if "SavingsPlansPurchaseRecommendationSummary" in data:
        import aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_summary

        out["savings_plans_purchase_recommendation_summary"] = (
            aws_sdk_cost_explorer.types.savings_plans_purchase_recommendation_summary.deserialize_aws_json_1_1(
                data["SavingsPlansPurchaseRecommendationSummary"]
            )
        )
    return out
