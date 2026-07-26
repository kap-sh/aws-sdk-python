"""Generated from Smithy shape ``com.amazonaws.configservice#DescribePendingAggregationRequestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.pending_aggregation_request_list
    import capo_config_service.types.string


class DescribePendingAggregationRequestsResponse(TypedDict, closed=True):
    pending_aggregation_requests: NotRequired[
        "capo_config_service.types.pending_aggregation_request_list.PendingAggregationRequestList"
    ]
    """<p>Returns a PendingAggregationRequests object.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePendingAggregationRequestsResponse) -> dict:
    out: dict = {}
    if "pending_aggregation_requests" in value:
        import capo_config_service.types.pending_aggregation_request_list

        out["PendingAggregationRequests"] = (
            capo_config_service.types.pending_aggregation_request_list.serialize_aws_json_1_1(
                value["pending_aggregation_requests"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePendingAggregationRequestsResponse:
    out: DescribePendingAggregationRequestsResponse = {}  # type: ignore[typeddict-item]
    if "PendingAggregationRequests" in data:
        import capo_config_service.types.pending_aggregation_request_list

        out["pending_aggregation_requests"] = (
            capo_config_service.types.pending_aggregation_request_list.deserialize_aws_json_1_1(
                data["PendingAggregationRequests"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
