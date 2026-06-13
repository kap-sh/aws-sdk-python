"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAgentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_search_filter_list
    import aws_sdk_quicksight.types.agents_max_results
    import aws_sdk_quicksight.types.aws_account_id


class SearchAgentsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the agents.</p>"""
    filters: "aws_sdk_quicksight.types.agent_search_filter_list.AgentSearchFilterList"
    """<p>The filters to apply when searching agents.</p>"""
    max_results: NotRequired[
        "aws_sdk_quicksight.types.agents_max_results.AgentsMaxResults"
    ]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAgentsRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.agent_search_filter_list

    out["Filters"] = aws_sdk_quicksight.types.agent_search_filter_list.serialize_json(
        value["filters"]
    )
    return out


def deserialize_json(data: dict) -> SearchAgentsRequest:
    out: SearchAgentsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_quicksight.types.agent_search_filter_list

        out["filters"] = (
            aws_sdk_quicksight.types.agent_search_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("SearchAgentsRequest.filters required")
    return out
