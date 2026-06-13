"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListBacklogTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.next_token
    import aws_sdk_devops_agent.types.task_filter
    import aws_sdk_devops_agent.types.task_sort_field
    import aws_sdk_devops_agent.types.task_sort_order


class ListBacklogTasksRequest(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the tasks</p>"""
    filter: NotRequired["aws_sdk_devops_agent.types.task_filter.TaskFilter"]
    """<p>Filter criteria to apply when listing tasks Filtering restrictions: - Each filter field list is limited to a single value - Filtering by Priority and Status at the same time when not filtering by Type is not permitted - Timestamp filters (createdAfter, createdBefore) can be combined with other filters when not sorting by priority</p>"""
    limit: "int"
    """<p>Maximum number of tasks to return in a single response (1-1000, default: 100)</p>"""
    next_token: NotRequired["aws_sdk_devops_agent.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results</p>"""
    sort_field: NotRequired["aws_sdk_devops_agent.types.task_sort_field.TaskSortField"]
    """<p>Field to sort by Sorting restrictions: - Only sorting on createdAt is supported when using priority or status filters alone. - Sorting by priority is not supported when using Timestamp filters (createdAfter, createdBefore)</p>"""
    order: "aws_sdk_devops_agent.types.task_sort_order.TaskSortOrder"
    """<p>Sort order for the tasks based on sortField (default: DESC)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBacklogTasksRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_devops_agent.types.task_filter

        out["filter"] = aws_sdk_devops_agent.types.task_filter.serialize_json(
            value["filter"]
        )
    out["limit"] = value.get("limit", 100)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "sort_field" in value:
        import aws_sdk_devops_agent.types.task_sort_field

        out["sortField"] = aws_sdk_devops_agent.types.task_sort_field.serialize_json(
            value["sort_field"]
        )
    import aws_sdk_devops_agent.types.task_sort_order

    out["order"] = aws_sdk_devops_agent.types.task_sort_order.serialize_json(
        value.get("order", "DESC")
    )
    return out


def deserialize_json(data: dict) -> ListBacklogTasksRequest:
    out: ListBacklogTasksRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_devops_agent.types.task_filter

        out["filter"] = aws_sdk_devops_agent.types.task_filter.deserialize_json(
            data["filter"]
        )
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 100
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "sortField" in data:
        import aws_sdk_devops_agent.types.task_sort_field

        out["sort_field"] = aws_sdk_devops_agent.types.task_sort_field.deserialize_json(
            data["sortField"]
        )
    if "order" in data:
        import aws_sdk_devops_agent.types.task_sort_order

        out["order"] = aws_sdk_devops_agent.types.task_sort_order.deserialize_json(
            data["order"]
        )
    else:
        out["order"] = "DESC"
    return out
