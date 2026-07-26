"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.back_log_timestamp
    import capo_devops_agent.types.priority_list
    import capo_devops_agent.types.resource_id
    import capo_devops_agent.types.task_status_list
    import capo_devops_agent.types.task_type_list


class TaskFilter(TypedDict, closed=True):
    created_after: NotRequired[
        "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    ]
    """<p>Filter for tasks created after this timestamp inclusive</p>"""
    created_before: NotRequired[
        "capo_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    ]
    """<p>Filter for tasks created before this timestamp exclusive</p>"""
    priority: NotRequired["capo_devops_agent.types.priority_list.PriorityList"]
    """<p>Filter by priority (single value only)</p>"""
    status: NotRequired["capo_devops_agent.types.task_status_list.TaskStatusList"]
    """<p>Filter by status (single value only)</p>"""
    task_type: NotRequired["capo_devops_agent.types.task_type_list.TaskTypeList"]
    """<p>Filter by task type (single value only)</p>"""
    primary_task_id: NotRequired["capo_devops_agent.types.resource_id.ResourceId"]
    """<p>Filter by primary task ID to get linked tasks</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaskFilter) -> dict:
    out: dict = {}
    if "created_after" in value:
        import capo_devops_agent.types.back_log_timestamp

        out["createdAfter"] = capo_devops_agent.types.back_log_timestamp.serialize_json(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_devops_agent.types.back_log_timestamp

        out["createdBefore"] = (
            capo_devops_agent.types.back_log_timestamp.serialize_json(
                value["created_before"]
            )
        )
    if "priority" in value:
        import capo_devops_agent.types.priority_list

        out["priority"] = capo_devops_agent.types.priority_list.serialize_json(
            value["priority"]
        )
    if "status" in value:
        import capo_devops_agent.types.task_status_list

        out["status"] = capo_devops_agent.types.task_status_list.serialize_json(
            value["status"]
        )
    if "task_type" in value:
        import capo_devops_agent.types.task_type_list

        out["taskType"] = capo_devops_agent.types.task_type_list.serialize_json(
            value["task_type"]
        )
    if "primary_task_id" in value:
        out["primaryTaskId"] = value["primary_task_id"]
    return out


def deserialize_json(data: dict) -> TaskFilter:
    out: TaskFilter = {}  # type: ignore[typeddict-item]
    if "createdAfter" in data:
        import capo_devops_agent.types.back_log_timestamp

        out["created_after"] = (
            capo_devops_agent.types.back_log_timestamp.deserialize_json(
                data["createdAfter"]
            )
        )
    if "createdBefore" in data:
        import capo_devops_agent.types.back_log_timestamp

        out["created_before"] = (
            capo_devops_agent.types.back_log_timestamp.deserialize_json(
                data["createdBefore"]
            )
        )
    if "priority" in data:
        import capo_devops_agent.types.priority_list

        out["priority"] = capo_devops_agent.types.priority_list.deserialize_json(
            data["priority"]
        )
    if "status" in data:
        import capo_devops_agent.types.task_status_list

        out["status"] = capo_devops_agent.types.task_status_list.deserialize_json(
            data["status"]
        )
    if "taskType" in data:
        import capo_devops_agent.types.task_type_list

        out["task_type"] = capo_devops_agent.types.task_type_list.deserialize_json(
            data["taskType"]
        )
    if "primaryTaskId" in data:
        out["primary_task_id"] = data["primaryTaskId"]
    return out
