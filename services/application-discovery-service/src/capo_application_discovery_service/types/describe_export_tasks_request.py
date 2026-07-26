"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeExportTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.export_filters
    import capo_application_discovery_service.types.export_ids
    import capo_application_discovery_service.types.integer
    import capo_application_discovery_service.types.next_token


class DescribeExportTasksRequest(TypedDict, closed=True):
    export_ids: NotRequired[
        "capo_application_discovery_service.types.export_ids.ExportIds"
    ]
    """<p>One or more unique identifiers used to query the status of an export request.</p>"""
    filters: NotRequired[
        "capo_application_discovery_service.types.export_filters.ExportFilters"
    ]
    """<p>One or more filters.</p> <ul> <li> <p> <code>AgentId</code> - ID of the agent whose collected data will be exported</p> </li> </ul>"""
    max_results: "capo_application_discovery_service.types.integer.Integer"
    """<p>The maximum number of volume results returned by <code>DescribeExportTasks</code> in paginated output. When this parameter is used, <code>DescribeExportTasks</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element.</p>"""
    next_token: NotRequired[
        "capo_application_discovery_service.types.next_token.NextToken"
    ]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>DescribeExportTasks</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeExportTasksRequest) -> dict:
    out: dict = {}
    if "export_ids" in value:
        import capo_application_discovery_service.types.export_ids

        out["exportIds"] = (
            capo_application_discovery_service.types.export_ids.serialize_aws_json_1_1(
                value["export_ids"]
            )
        )
    if "filters" in value:
        import capo_application_discovery_service.types.export_filters

        out["filters"] = (
            capo_application_discovery_service.types.export_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    out["maxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeExportTasksRequest:
    out: DescribeExportTasksRequest = {}  # type: ignore[typeddict-item]
    if "exportIds" in data:
        import capo_application_discovery_service.types.export_ids

        out["export_ids"] = (
            capo_application_discovery_service.types.export_ids.deserialize_aws_json_1_1(
                data["exportIds"]
            )
        )
    if "filters" in data:
        import capo_application_discovery_service.types.export_filters

        out["filters"] = (
            capo_application_discovery_service.types.export_filters.deserialize_aws_json_1_1(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 0
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
