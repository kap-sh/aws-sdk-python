"""Generated from Smithy shape ``com.amazonaws.batch#ListJobsByConsumableResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.list_jobs_by_consumable_resource_filter_list
    import aws_sdk_batch.types.string


class ListJobsByConsumableResourceRequest(TypedDict, closed=True):
    consumable_resource: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The name or ARN of the consumable resource.</p>"""
    filters: NotRequired[
        "aws_sdk_batch.types.list_jobs_by_consumable_resource_filter_list.ListJobsByConsumableResourceFilterList"
    ]
    """<p>The filters to apply to the job list query. If used, only those jobs requiring the specified consumable resource (<code>consumableResource</code>) and that match the value of the filters are listed. The filter names and values can be:</p> <ul> <li> <p>name: <code>JOB_STATUS</code> </p> <p>values: <code>SUBMITTED | PENDING | RUNNABLE | STARTING | RUNNING | SUCCEEDED | FAILED</code> </p> </li> <li> <p>name: <code>JOB_NAME </code> </p> <p>The values are case-insensitive matches for the job name. If a filter value ends with an asterisk (*), it matches any job name that begins with the string before the '*'.</p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The maximum number of results returned by <code>ListJobsByConsumableResource</code> in paginated output. When this parameter is used, <code>ListJobsByConsumableResource</code> only returns <code>maxResults</code> results in a single page and a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListJobsByConsumableResource</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListJobsByConsumableResource</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListJobsByConsumableResource</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsByConsumableResourceRequest) -> dict:
    out: dict = {}
    if "consumable_resource" in value:
        out["consumableResource"] = value["consumable_resource"]
    if "filters" in value:
        import aws_sdk_batch.types.list_jobs_by_consumable_resource_filter_list

        out["filters"] = (
            aws_sdk_batch.types.list_jobs_by_consumable_resource_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsByConsumableResourceRequest:
    out: ListJobsByConsumableResourceRequest = {}  # type: ignore[typeddict-item]
    if "consumableResource" in data:
        out["consumable_resource"] = data["consumableResource"]
    if "filters" in data:
        import aws_sdk_batch.types.list_jobs_by_consumable_resource_filter_list

        out["filters"] = (
            aws_sdk_batch.types.list_jobs_by_consumable_resource_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
