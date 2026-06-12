"""Generated from Smithy shape ``com.amazonaws.costexplorer#ReservationPurchaseRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.account_scope
    import aws_sdk_cost_explorer.types.lookback_period_in_days
    import aws_sdk_cost_explorer.types.payment_option
    import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_details
    import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_summary
    import aws_sdk_cost_explorer.types.service_specification
    import aws_sdk_cost_explorer.types.term_in_years


class ReservationPurchaseRecommendation(TypedDict):
    account_scope: NotRequired["aws_sdk_cost_explorer.types.account_scope.AccountScope"]
    """<p>The account scope that Amazon Web Services recommends that you purchase this instance for. For example, you can purchase this reservation for an entire organization in Amazon Web Services Organizations.</p>"""
    lookback_period_in_days: NotRequired[
        "aws_sdk_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
    ]
    """<p>How many days of previous usage that Amazon Web Services considers when making this recommendation.</p>"""
    term_in_years: NotRequired["aws_sdk_cost_explorer.types.term_in_years.TermInYears"]
    """<p>The term of the reservation that you want recommendations for, in years.</p>"""
    payment_option: NotRequired[
        "aws_sdk_cost_explorer.types.payment_option.PaymentOption"
    ]
    """<p>The payment option for the reservation (for example, <code>AllUpfront</code> or <code>NoUpfront</code>).</p>"""
    service_specification: NotRequired[
        "aws_sdk_cost_explorer.types.service_specification.ServiceSpecification"
    ]
    """<p>Hardware specifications for the service that you want recommendations for.</p>"""
    recommendation_details: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_purchase_recommendation_details.ReservationPurchaseRecommendationDetails"
    ]
    """<p>Details about the recommended purchases.</p>"""
    recommendation_summary: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_purchase_recommendation_summary.ReservationPurchaseRecommendationSummary"
    ]
    """<p>A summary about the recommended purchase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservationPurchaseRecommendation) -> dict:
    out: dict = {}
    if "account_scope" in value:
        import aws_sdk_cost_explorer.types.account_scope

        out["AccountScope"] = (
            aws_sdk_cost_explorer.types.account_scope.serialize_aws_json_1_1(
                value["account_scope"]
            )
        )
    if "lookback_period_in_days" in value:
        import aws_sdk_cost_explorer.types.lookback_period_in_days

        out["LookbackPeriodInDays"] = (
            aws_sdk_cost_explorer.types.lookback_period_in_days.serialize_aws_json_1_1(
                value["lookback_period_in_days"]
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
    if "service_specification" in value:
        import aws_sdk_cost_explorer.types.service_specification

        out["ServiceSpecification"] = (
            aws_sdk_cost_explorer.types.service_specification.serialize_aws_json_1_1(
                value["service_specification"]
            )
        )
    if "recommendation_details" in value:
        import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_details

        out["RecommendationDetails"] = (
            aws_sdk_cost_explorer.types.reservation_purchase_recommendation_details.serialize_aws_json_1_1(
                value["recommendation_details"]
            )
        )
    if "recommendation_summary" in value:
        import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_summary

        out["RecommendationSummary"] = (
            aws_sdk_cost_explorer.types.reservation_purchase_recommendation_summary.serialize_aws_json_1_1(
                value["recommendation_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReservationPurchaseRecommendation:
    out: ReservationPurchaseRecommendation = {}  # type: ignore[typeddict-item]
    if "AccountScope" in data:
        import aws_sdk_cost_explorer.types.account_scope

        out["account_scope"] = (
            aws_sdk_cost_explorer.types.account_scope.deserialize_aws_json_1_1(
                data["AccountScope"]
            )
        )
    if "LookbackPeriodInDays" in data:
        import aws_sdk_cost_explorer.types.lookback_period_in_days

        out["lookback_period_in_days"] = (
            aws_sdk_cost_explorer.types.lookback_period_in_days.deserialize_aws_json_1_1(
                data["LookbackPeriodInDays"]
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
    if "ServiceSpecification" in data:
        import aws_sdk_cost_explorer.types.service_specification

        out["service_specification"] = (
            aws_sdk_cost_explorer.types.service_specification.deserialize_aws_json_1_1(
                data["ServiceSpecification"]
            )
        )
    if "RecommendationDetails" in data:
        import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_details

        out["recommendation_details"] = (
            aws_sdk_cost_explorer.types.reservation_purchase_recommendation_details.deserialize_aws_json_1_1(
                data["RecommendationDetails"]
            )
        )
    if "RecommendationSummary" in data:
        import aws_sdk_cost_explorer.types.reservation_purchase_recommendation_summary

        out["recommendation_summary"] = (
            aws_sdk_cost_explorer.types.reservation_purchase_recommendation_summary.deserialize_aws_json_1_1(
                data["RecommendationSummary"]
            )
        )
    return out
