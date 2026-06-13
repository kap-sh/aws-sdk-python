"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchFlowsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.account_id
    import aws_sdk_quicksight.types.flow_max_results
    import aws_sdk_quicksight.types.search_flows_filter_list


class SearchFlowsInput(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account where you are searching for flows from.</p>"""
    filters: "aws_sdk_quicksight.types.search_flows_filter_list.SearchFlowsFilterList"
    """<p>The filters applied to the search when searching for flows in the Amazon Web Services account.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to request the next set of results, or null if you want to retrieve the first set.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.flow_max_results.FlowMaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFlowsInput) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.search_flows_filter_list

    out["Filters"] = aws_sdk_quicksight.types.search_flows_filter_list.serialize_json(
        value["filters"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> SearchFlowsInput:
    out: SearchFlowsInput = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_quicksight.types.search_flows_filter_list

        out["filters"] = (
            aws_sdk_quicksight.types.search_flows_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("SearchFlowsInput.filters required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
