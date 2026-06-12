"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetSavingsPlansUtilizationDetailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.date_interval
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.savings_plans_utilization_aggregates
    import aws_sdk_cost_explorer.types.savings_plans_utilization_details


class GetSavingsPlansUtilizationDetailsResponse(TypedDict):
    savings_plans_utilization_details: "aws_sdk_cost_explorer.types.savings_plans_utilization_details.SavingsPlansUtilizationDetails"
    """<p>Retrieves a single daily or monthly Savings Plans utilization rate and details for your account.</p>"""
    total: NotRequired[
        "aws_sdk_cost_explorer.types.savings_plans_utilization_aggregates.SavingsPlansUtilizationAggregates"
    ]
    """<p>The total Savings Plans utilization, regardless of time period.</p>"""
    time_period: "aws_sdk_cost_explorer.types.date_interval.DateInterval"
    next_token: NotRequired["aws_sdk_cost_explorer.types.next_page_token.NextPageToken"]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSavingsPlansUtilizationDetailsResponse) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.savings_plans_utilization_details

    out["SavingsPlansUtilizationDetails"] = (
        aws_sdk_cost_explorer.types.savings_plans_utilization_details.serialize_aws_json_1_1(
            value["savings_plans_utilization_details"]
        )
    )
    if "total" in value:
        import aws_sdk_cost_explorer.types.savings_plans_utilization_aggregates

        out["Total"] = (
            aws_sdk_cost_explorer.types.savings_plans_utilization_aggregates.serialize_aws_json_1_1(
                value["total"]
            )
        )
    import aws_sdk_cost_explorer.types.date_interval

    out["TimePeriod"] = (
        aws_sdk_cost_explorer.types.date_interval.serialize_aws_json_1_1(
            value["time_period"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSavingsPlansUtilizationDetailsResponse:
    out: GetSavingsPlansUtilizationDetailsResponse = {}  # type: ignore[typeddict-item]
    if "SavingsPlansUtilizationDetails" in data:
        import aws_sdk_cost_explorer.types.savings_plans_utilization_details

        out["savings_plans_utilization_details"] = (
            aws_sdk_cost_explorer.types.savings_plans_utilization_details.deserialize_aws_json_1_1(
                data["SavingsPlansUtilizationDetails"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansUtilizationDetailsResponse.savings_plans_utilization_details required"
        )
    if "Total" in data:
        import aws_sdk_cost_explorer.types.savings_plans_utilization_aggregates

        out["total"] = (
            aws_sdk_cost_explorer.types.savings_plans_utilization_aggregates.deserialize_aws_json_1_1(
                data["Total"]
            )
        )
    if "TimePeriod" in data:
        import aws_sdk_cost_explorer.types.date_interval

        out["time_period"] = (
            aws_sdk_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError(
            "GetSavingsPlansUtilizationDetailsResponse.time_period required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
