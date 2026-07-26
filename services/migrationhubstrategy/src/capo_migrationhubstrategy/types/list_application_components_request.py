"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListApplicationComponentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.application_component_criteria
    import capo_migrationhubstrategy.types.group_ids
    import capo_migrationhubstrategy.types.max_result
    import capo_migrationhubstrategy.types.next_token
    import capo_migrationhubstrategy.types.sort_order
    import capo_migrationhubstrategy.types.string


class ListApplicationComponentsRequest(TypedDict, closed=True):
    application_component_criteria: NotRequired[
        "capo_migrationhubstrategy.types.application_component_criteria.ApplicationComponentCriteria"
    ]
    """<p> Criteria for filtering the list of application components. </p>"""
    filter_value: NotRequired["capo_migrationhubstrategy.types.string.String"]
    """<p> Specify the value based on the application component criteria type. For example, if <code>applicationComponentCriteria</code> is set to <code>SERVER_ID</code> and <code>filterValue</code> is set to <code>server1</code>, then <a>ListApplicationComponents</a> returns all the application components running on server1. </p>"""
    sort: NotRequired["capo_migrationhubstrategy.types.sort_order.SortOrder"]
    """<p> Specifies whether to sort by ascending (<code>ASC</code>) or descending (<code>DESC</code>) order. </p>"""
    group_id_filter: NotRequired["capo_migrationhubstrategy.types.group_ids.GroupIds"]
    """<p> The group ID specified in to filter on. </p>"""
    next_token: NotRequired["capo_migrationhubstrategy.types.next_token.NextToken"]
    """<p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>"""
    max_results: NotRequired["capo_migrationhubstrategy.types.max_result.MaxResult"]
    """<p> The maximum number of items to include in the response. The maximum value is 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationComponentsRequest) -> dict:
    out: dict = {}
    if "application_component_criteria" in value:
        out["applicationComponentCriteria"] = value["application_component_criteria"]
    if "filter_value" in value:
        out["filterValue"] = value["filter_value"]
    if "sort" in value:
        out["sort"] = value["sort"]
    if "group_id_filter" in value:
        import capo_migrationhubstrategy.types.group_ids

        out["groupIdFilter"] = capo_migrationhubstrategy.types.group_ids.serialize_json(
            value["group_id_filter"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListApplicationComponentsRequest:
    out: ListApplicationComponentsRequest = {}  # type: ignore[typeddict-item]
    if "applicationComponentCriteria" in data:
        out["application_component_criteria"] = data["applicationComponentCriteria"]
    if "filterValue" in data:
        out["filter_value"] = data["filterValue"]
    if "sort" in data:
        out["sort"] = data["sort"]
    if "groupIdFilter" in data:
        import capo_migrationhubstrategy.types.group_ids

        out["group_id_filter"] = (
            capo_migrationhubstrategy.types.group_ids.deserialize_json(
                data["groupIdFilter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
