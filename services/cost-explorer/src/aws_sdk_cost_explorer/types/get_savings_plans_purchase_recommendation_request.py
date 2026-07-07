"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlansPurchaseRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.account_scope
    import aws_sdk_cost_explorer.types.expression
    import aws_sdk_cost_explorer.types.lookback_period_in_days
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.payment_option
    import aws_sdk_cost_explorer.types.recommendations_page_size
    import aws_sdk_cost_explorer.types.supported_savings_plans_type
    import aws_sdk_cost_explorer.types.term_in_years


class GetSavingsPlansPurchaseRecommendationRequest(TypedDict, closed=True):
    savings_plans_type: "aws_sdk_cost_explorer.types.supported_savings_plans_type.SupportedSavingsPlansType"
    """<p>The Savings Plans recommendation type that's requested.</p>"""
    term_in_years: "aws_sdk_cost_explorer.types.term_in_years.TermInYears"
    """<p>The savings plan recommendation term that's used to generate these recommendations.</p>"""
    payment_option: "aws_sdk_cost_explorer.types.payment_option.PaymentOption"
    """<p>The payment option that's used to generate these recommendations.</p>"""
    account_scope: NotRequired["aws_sdk_cost_explorer.types.account_scope.AccountScope"]
    """<p>The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to <code>PAYER</code>. If the value is <code>LINKED</code>, recommendations are calculated for individual member accounts only.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""
    page_size: (
        "aws_sdk_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
    )
    """<p>The number of recommendations that you want returned in a single response object.</p>"""
    lookback_period_in_days: (
        "aws_sdk_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
    )
    """<p>The lookback period that's used to generate the recommendation.</p>"""
    filter: NotRequired["aws_sdk_cost_explorer.types.expression.Expression"]
    """<p>You can filter your recommendations by Account ID with the <code>LINKED_ACCOUNT</code> dimension. To filter your recommendations by Account ID, specify <code>Key</code> as <code>LINKED_ACCOUNT</code> and <code>Value</code> as the comma-separated Acount ID(s) that you want to see Savings Plans purchase recommendations for.</p> <p>For GetSavingsPlansPurchaseRecommendation, the <code>Filter</code> doesn't include <code>CostCategories</code> or <code>Tags</code>. It only includes <code>Dimensions</code>. With <code>Dimensions</code>, <code>Key</code> must be <code>LINKED_ACCOUNT</code> and <code>Value</code> can be a single Account ID or multiple comma-separated Account IDs that you want to see Savings Plans Purchase Recommendations for. <code>AND</code> and <code>OR</code> operators are not supported.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSavingsPlansPurchaseRecommendationRequest) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.supported_savings_plans_type

    out["SavingsPlansType"] = (
        aws_sdk_cost_explorer.types.supported_savings_plans_type.serialize_aws_json_1_1(
            value["savings_plans_type"]
        )
    )
    import aws_sdk_cost_explorer.types.term_in_years

    out["TermInYears"] = (
        aws_sdk_cost_explorer.types.term_in_years.serialize_aws_json_1_1(
            value["term_in_years"]
        )
    )
    import aws_sdk_cost_explorer.types.payment_option

    out["PaymentOption"] = (
        aws_sdk_cost_explorer.types.payment_option.serialize_aws_json_1_1(
            value["payment_option"]
        )
    )
    if "account_scope" in value:
        import aws_sdk_cost_explorer.types.account_scope

        out["AccountScope"] = (
            aws_sdk_cost_explorer.types.account_scope.serialize_aws_json_1_1(
                value["account_scope"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    out["PageSize"] = value.get("page_size", 0)
    import aws_sdk_cost_explorer.types.lookback_period_in_days

    out["LookbackPeriodInDays"] = (
        aws_sdk_cost_explorer.types.lookback_period_in_days.serialize_aws_json_1_1(
            value["lookback_period_in_days"]
        )
    )
    if "filter" in value:
        import aws_sdk_cost_explorer.types.expression

        out["Filter"] = aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetSavingsPlansPurchaseRecommendationRequest:
    out: GetSavingsPlansPurchaseRecommendationRequest = {}  # type: ignore[typeddict-item]
    if "SavingsPlansType" in data:
        import aws_sdk_cost_explorer.types.supported_savings_plans_type

        out["savings_plans_type"] = (
            aws_sdk_cost_explorer.types.supported_savings_plans_type.deserialize_aws_json_1_1(
                data["SavingsPlansType"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansPurchaseRecommendationRequest.savings_plans_type required"
        )
    if "TermInYears" in data:
        import aws_sdk_cost_explorer.types.term_in_years

        out["term_in_years"] = (
            aws_sdk_cost_explorer.types.term_in_years.deserialize_aws_json_1_1(
                data["TermInYears"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansPurchaseRecommendationRequest.term_in_years required"
        )
    if "PaymentOption" in data:
        import aws_sdk_cost_explorer.types.payment_option

        out["payment_option"] = (
            aws_sdk_cost_explorer.types.payment_option.deserialize_aws_json_1_1(
                data["PaymentOption"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansPurchaseRecommendationRequest.payment_option required"
        )
    if "AccountScope" in data:
        import aws_sdk_cost_explorer.types.account_scope

        out["account_scope"] = (
            aws_sdk_cost_explorer.types.account_scope.deserialize_aws_json_1_1(
                data["AccountScope"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "LookbackPeriodInDays" in data:
        import aws_sdk_cost_explorer.types.lookback_period_in_days

        out["lookback_period_in_days"] = (
            aws_sdk_cost_explorer.types.lookback_period_in_days.deserialize_aws_json_1_1(
                data["LookbackPeriodInDays"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansPurchaseRecommendationRequest.lookback_period_in_days required"
        )
    if "Filter" in data:
        import aws_sdk_cost_explorer.types.expression

        out["filter"] = aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    return out
