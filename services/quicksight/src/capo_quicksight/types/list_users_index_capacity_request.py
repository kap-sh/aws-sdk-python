"""Generated from Smithy shape ``com.amazonaws.quicksight#ListUsersIndexCapacityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.list_users_index_capacity_request_max_results_integer
    import capo_quicksight.types.namespace
    import capo_quicksight.types.user_index_capacity_filters
    import capo_quicksight.types.user_index_capacity_sort_by
    import capo_quicksight.types.user_index_capacity_sort_order


class ListUsersIndexCapacityRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the index capacity data.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The namespace to scope the user search to. Required when the userNameOrEmail filter is present.</p>"""
    filters: NotRequired[
        "capo_quicksight.types.user_index_capacity_filters.UserIndexCapacityFilters"
    ]
    """<p>Filters to apply. Only one filter is supported per request. The userNameOrEmail and totalCapacityBytes filters are mutually exclusive.</p>"""
    sort_by: NotRequired[
        "capo_quicksight.types.user_index_capacity_sort_by.UserIndexCapacitySortBy"
    ]
    """<p>The field to sort results by.</p>"""
    sort_order: NotRequired[
        "capo_quicksight.types.user_index_capacity_sort_order.UserIndexCapacitySortOrder"
    ]
    """<p>The sort order for results. Defaults to DESC if not specified.</p>"""
    max_results: NotRequired[
        "capo_quicksight.types.list_users_index_capacity_request_max_results_integer.ListUsersIndexCapacityRequestMaxResultsInteger"
    ]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results, received from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUsersIndexCapacityRequest) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "filters" in value:
        import capo_quicksight.types.user_index_capacity_filters

        out["filters"] = (
            capo_quicksight.types.user_index_capacity_filters.serialize_json(
                value["filters"]
            )
        )
    if "sort_by" in value:
        import capo_quicksight.types.user_index_capacity_sort_by

        out["sortBy"] = (
            capo_quicksight.types.user_index_capacity_sort_by.serialize_json(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_quicksight.types.user_index_capacity_sort_order

        out["sortOrder"] = (
            capo_quicksight.types.user_index_capacity_sort_order.serialize_json(
                value["sort_order"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUsersIndexCapacityRequest:
    out: ListUsersIndexCapacityRequest = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "filters" in data:
        import capo_quicksight.types.user_index_capacity_filters

        out["filters"] = (
            capo_quicksight.types.user_index_capacity_filters.deserialize_json(
                data["filters"]
            )
        )
    if "sortBy" in data:
        import capo_quicksight.types.user_index_capacity_sort_by

        out["sort_by"] = (
            capo_quicksight.types.user_index_capacity_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    if "sortOrder" in data:
        import capo_quicksight.types.user_index_capacity_sort_order

        out["sort_order"] = (
            capo_quicksight.types.user_index_capacity_sort_order.deserialize_json(
                data["sortOrder"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
