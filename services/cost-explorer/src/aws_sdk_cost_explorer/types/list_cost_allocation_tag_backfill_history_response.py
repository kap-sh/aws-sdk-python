"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListCostAllocationTagBackfillHistoryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request_list
    import aws_sdk_cost_explorer.types.next_page_token


class ListCostAllocationTagBackfillHistoryResponse(TypedDict):
    backfill_requests: NotRequired[
        "aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request_list.CostAllocationTagBackfillRequestList"
    ]
    """<p> The list of historical cost allocation tag backfill requests. </p>"""
    next_token: NotRequired["aws_sdk_cost_explorer.types.next_page_token.NextPageToken"]
    """<p> The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCostAllocationTagBackfillHistoryResponse) -> dict:
    out: dict = {}
    if "backfill_requests" in value:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request_list

        out["BackfillRequests"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request_list.serialize_aws_json_1_1(
                value["backfill_requests"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListCostAllocationTagBackfillHistoryResponse:
    out: ListCostAllocationTagBackfillHistoryResponse = {}  # type: ignore[typeddict-item]
    if "BackfillRequests" in data:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request_list

        out["backfill_requests"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request_list.deserialize_aws_json_1_1(
                data["BackfillRequests"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
