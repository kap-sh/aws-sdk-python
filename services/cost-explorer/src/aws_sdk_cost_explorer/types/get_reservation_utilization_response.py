"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetReservationUtilizationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.reservation_aggregates
    import aws_sdk_cost_explorer.types.utilizations_by_time


class GetReservationUtilizationResponse(TypedDict):
    utilizations_by_time: (
        "aws_sdk_cost_explorer.types.utilizations_by_time.UtilizationsByTime"
    )
    """<p>The amount of time that you used your Reserved Instances (RIs).</p>"""
    total: NotRequired[
        "aws_sdk_cost_explorer.types.reservation_aggregates.ReservationAggregates"
    ]
    """<p>The total amount of time that you used your Reserved Instances (RIs).</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token for the next set of retrievable results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReservationUtilizationResponse) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.utilizations_by_time

    out["UtilizationsByTime"] = (
        aws_sdk_cost_explorer.types.utilizations_by_time.serialize_aws_json_1_1(
            value["utilizations_by_time"]
        )
    )
    if "total" in value:
        import aws_sdk_cost_explorer.types.reservation_aggregates

        out["Total"] = (
            aws_sdk_cost_explorer.types.reservation_aggregates.serialize_aws_json_1_1(
                value["total"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReservationUtilizationResponse:
    out: GetReservationUtilizationResponse = {}  # type: ignore[typeddict-item]
    if "UtilizationsByTime" in data:
        import aws_sdk_cost_explorer.types.utilizations_by_time

        out["utilizations_by_time"] = (
            aws_sdk_cost_explorer.types.utilizations_by_time.deserialize_aws_json_1_1(
                data["UtilizationsByTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetReservationUtilizationResponse.utilizations_by_time required"
        )
    if "Total" in data:
        import aws_sdk_cost_explorer.types.reservation_aggregates

        out["total"] = (
            aws_sdk_cost_explorer.types.reservation_aggregates.deserialize_aws_json_1_1(
                data["Total"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
