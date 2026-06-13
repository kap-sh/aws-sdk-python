"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchActionConnectorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_connector_search_filter_list
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.search_action_connectors_request_max_results_integer


class SearchActionConnectorsRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID in which to search for action connectors.</p>"""
    max_results: "aws_sdk_quicksight.types.search_action_connectors_request_max_results_integer.SearchActionConnectorsRequestMaxResultsInteger"
    """<p>The maximum number of action connectors to return in a single response. Valid range is 1 to 100.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token to retrieve the next set of results. Use the token returned from a previous call to continue searching.</p>"""
    filters: "aws_sdk_quicksight.types.action_connector_search_filter_list.ActionConnectorSearchFilterList"
    """<p>The search filters to apply. You can filter by connector name, type, or user permissions. Maximum of one filter is supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchActionConnectorsRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.action_connector_search_filter_list

    out["Filters"] = (
        aws_sdk_quicksight.types.action_connector_search_filter_list.serialize_json(
            value["filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchActionConnectorsRequest:
    out: SearchActionConnectorsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_quicksight.types.action_connector_search_filter_list

        out["filters"] = (
            aws_sdk_quicksight.types.action_connector_search_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("SearchActionConnectorsRequest.filters required")
    return out
