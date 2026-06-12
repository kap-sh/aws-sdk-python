"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListServersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.group_ids
    import aws_sdk_migrationhubstrategy.types.max_result
    import aws_sdk_migrationhubstrategy.types.next_token
    import aws_sdk_migrationhubstrategy.types.server_criteria
    import aws_sdk_migrationhubstrategy.types.sort_order
    import aws_sdk_migrationhubstrategy.types.string


class ListServersRequest(TypedDict):
    server_criteria: NotRequired[
        "aws_sdk_migrationhubstrategy.types.server_criteria.ServerCriteria"
    ]
    """<p> Criteria for filtering servers. </p>"""
    filter_value: NotRequired["aws_sdk_migrationhubstrategy.types.string.String"]
    """<p> Specifies the filter value, which is based on the type of server criteria. For example, if <code>serverCriteria</code> is <code>OS_NAME</code>, and the <code>filterValue</code> is equal to <code>WindowsServer</code>, then <code>ListServers</code> returns all of the servers matching the OS name <code>WindowsServer</code>. </p>"""
    sort: NotRequired["aws_sdk_migrationhubstrategy.types.sort_order.SortOrder"]
    """<p> Specifies whether to sort by ascending (<code>ASC</code>) or descending (<code>DESC</code>) order. </p>"""
    group_id_filter: NotRequired[
        "aws_sdk_migrationhubstrategy.types.group_ids.GroupIds"
    ]
    """<p> Specifies the group ID to filter on. </p>"""
    next_token: NotRequired["aws_sdk_migrationhubstrategy.types.next_token.NextToken"]
    """<p> The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set <code>maxResults</code> to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10. </p>"""
    max_results: NotRequired["aws_sdk_migrationhubstrategy.types.max_result.MaxResult"]
    """<p> The maximum number of items to include in the response. The maximum value is 100. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServersRequest) -> dict:
    out: dict = {}
    if "server_criteria" in value:
        out["serverCriteria"] = value["server_criteria"]
    if "filter_value" in value:
        out["filterValue"] = value["filter_value"]
    if "sort" in value:
        out["sort"] = value["sort"]
    if "group_id_filter" in value:
        import aws_sdk_migrationhubstrategy.types.group_ids

        out["groupIdFilter"] = (
            aws_sdk_migrationhubstrategy.types.group_ids.serialize_json(
                value["group_id_filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListServersRequest:
    out: ListServersRequest = {}  # type: ignore[typeddict-item]
    if "serverCriteria" in data:
        out["server_criteria"] = data["serverCriteria"]
    if "filterValue" in data:
        out["filter_value"] = data["filterValue"]
    if "sort" in data:
        out["sort"] = data["sort"]
    if "groupIdFilter" in data:
        import aws_sdk_migrationhubstrategy.types.group_ids

        out["group_id_filter"] = (
            aws_sdk_migrationhubstrategy.types.group_ids.deserialize_json(
                data["groupIdFilter"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
