"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetReservationPurchaseRecommendationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.account_scope
    import aws_sdk_cost_explorer.types.expression
    import aws_sdk_cost_explorer.types.generic_string
    import aws_sdk_cost_explorer.types.lookback_period_in_days
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.payment_option
    import aws_sdk_cost_explorer.types.recommendations_page_size
    import aws_sdk_cost_explorer.types.service_specification
    import aws_sdk_cost_explorer.types.term_in_years


class GetReservationPurchaseRecommendationRequest(TypedDict):
    account_id: NotRequired["aws_sdk_cost_explorer.types.generic_string.GenericString"]
    """<p>The account ID that's associated with the recommendation. </p>"""
    service: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The specific service that you want recommendations for.</p>"""
    filter: NotRequired["aws_sdk_cost_explorer.types.expression.Expression"]
    account_scope: NotRequired["aws_sdk_cost_explorer.types.account_scope.AccountScope"]
    """<p>The account scope that you want your recommendations for. Amazon Web Services calculates recommendations including the management account and member accounts if the value is set to <code>PAYER</code>. If the value is <code>LINKED</code>, recommendations are calculated for individual member accounts only.</p>"""
    lookback_period_in_days: NotRequired[
        "aws_sdk_cost_explorer.types.lookback_period_in_days.LookbackPeriodInDays"
    ]
    """<p>The number of previous days that you want Amazon Web Services to consider when it calculates your recommendations.</p>"""
    term_in_years: NotRequired["aws_sdk_cost_explorer.types.term_in_years.TermInYears"]
    """<p>The reservation term that you want recommendations for.</p>"""
    payment_option: NotRequired[
        "aws_sdk_cost_explorer.types.payment_option.PaymentOption"
    ]
    """<p>The reservation purchase option that you want recommendations for.</p>"""
    service_specification: NotRequired[
        "aws_sdk_cost_explorer.types.service_specification.ServiceSpecification"
    ]
    """<p>The hardware specifications for the service instances that you want recommendations for, such as standard or convertible Amazon EC2 instances.</p>"""
    page_size: (
        "aws_sdk_cost_explorer.types.recommendations_page_size.RecommendationsPageSize"
    )
    """<p>The number of recommendations that you want returned in a single response object.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationPurchaseRecommendationRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    out["Service"] = value["service"]
    if "filter" in value:
        import aws_sdk_cost_explorer.types.expression

        out["Filter"] = aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
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
    out["PageSize"] = value.get("page_size", 0)
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationPurchaseRecommendationRequest:
    out: GetReservationPurchaseRecommendationRequest = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Service" in data:
        out["service"] = data["Service"]
    else:
        raise DeserializationError(
            "GetReservationPurchaseRecommendationRequest.service required"
        )
    if "Filter" in data:
        import aws_sdk_cost_explorer.types.expression

        out["filter"] = aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
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
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
