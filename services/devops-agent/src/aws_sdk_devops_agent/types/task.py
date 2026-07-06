"""Generated from Smithy shape ``com.amazonaws.devopsagent#Task``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.back_log_timestamp
    import aws_sdk_devops_agent.types.priority
    import aws_sdk_devops_agent.types.reference_output
    import aws_sdk_devops_agent.types.task_status
    import aws_sdk_devops_agent.types.task_type


class Task(TypedDict, closed=True):
    agent_space_id: "str"
    """<p>The unique identifier for the agent space containing this task</p>"""
    task_id: "str"
    """<p>The unique identifier for this task</p>"""
    execution_id: NotRequired["str"]
    """<p>The execution ID associated with this task, if any</p>"""
    title: "str"
    """<p>The title of the task</p>"""
    description: NotRequired["str"]
    """<p>Optional detailed description of the task</p>"""
    reference: NotRequired[
        "aws_sdk_devops_agent.types.reference_output.ReferenceOutput"
    ]
    """<p>Optional reference information linking this task to external systems</p>"""
    task_type: "aws_sdk_devops_agent.types.task_type.TaskType"
    """<p>The type of this task</p>"""
    priority: "aws_sdk_devops_agent.types.priority.Priority"
    """<p>The priority level of this task</p>"""
    status: "aws_sdk_devops_agent.types.task_status.TaskStatus"
    """<p>The current status of this task</p>"""
    created_at: "aws_sdk_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this task was created</p>"""
    updated_at: "aws_sdk_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this task was last updated</p>"""
    version: "int"
    """<p>Version number for optimistic locking</p>"""
    support_metadata: NotRequired["object"]
    """<p>Optional support metadata for the task</p>"""
    metadata: NotRequired["object"]
    """<p>Optional metadata for the task</p>"""
    primary_task_id: NotRequired["str"]
    """<p>The task ID of the primary investigation this task is linked to</p>"""
    status_reason: NotRequired["str"]
    """<p>Explanation for why the task status was changed (e.g., linked reason)</p>"""
    has_linked_tasks: "bool"
    """<p>Indicates if this task has other tasks linked to it</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Task) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["taskId"] = value["task_id"]
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    if "reference" in value:
        import aws_sdk_devops_agent.types.reference_output

        out["reference"] = aws_sdk_devops_agent.types.reference_output.serialize_json(
            value["reference"]
        )
    import aws_sdk_devops_agent.types.task_type

    out["taskType"] = aws_sdk_devops_agent.types.task_type.serialize_json(
        value["task_type"]
    )
    import aws_sdk_devops_agent.types.priority

    out["priority"] = aws_sdk_devops_agent.types.priority.serialize_json(
        value["priority"]
    )
    import aws_sdk_devops_agent.types.task_status

    out["status"] = aws_sdk_devops_agent.types.task_status.serialize_json(
        value["status"]
    )
    import aws_sdk_devops_agent.types.back_log_timestamp

    out["createdAt"] = aws_sdk_devops_agent.types.back_log_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_devops_agent.types.back_log_timestamp

    out["updatedAt"] = aws_sdk_devops_agent.types.back_log_timestamp.serialize_json(
        value["updated_at"]
    )
    out["version"] = value["version"]
    if "support_metadata" in value:
        out["supportMetadata"] = value["support_metadata"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    if "primary_task_id" in value:
        out["primaryTaskId"] = value["primary_task_id"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    out["hasLinkedTasks"] = value.get("has_linked_tasks", False)
    return out


def deserialize_json(data: dict) -> Task:
    out: Task = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("Task.agent_space_id required")
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("Task.task_id required")
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("Task.title required")
    if "description" in data:
        out["description"] = data["description"]
    if "reference" in data:
        import aws_sdk_devops_agent.types.reference_output

        out["reference"] = aws_sdk_devops_agent.types.reference_output.deserialize_json(
            data["reference"]
        )
    if "taskType" in data:
        import aws_sdk_devops_agent.types.task_type

        out["task_type"] = aws_sdk_devops_agent.types.task_type.deserialize_json(
            data["taskType"]
        )
    else:
        raise DeserializationError("Task.task_type required")
    if "priority" in data:
        import aws_sdk_devops_agent.types.priority

        out["priority"] = aws_sdk_devops_agent.types.priority.deserialize_json(
            data["priority"]
        )
    else:
        raise DeserializationError("Task.priority required")
    if "status" in data:
        import aws_sdk_devops_agent.types.task_status

        out["status"] = aws_sdk_devops_agent.types.task_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("Task.status required")
    if "createdAt" in data:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types.back_log_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Task.created_at required")
    if "updatedAt" in data:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["updated_at"] = (
            aws_sdk_devops_agent.types.back_log_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Task.updated_at required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("Task.version required")
    if "supportMetadata" in data:
        out["support_metadata"] = data["supportMetadata"]
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    if "primaryTaskId" in data:
        out["primary_task_id"] = data["primaryTaskId"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "hasLinkedTasks" in data:
        out["has_linked_tasks"] = data["hasLinkedTasks"]
    else:
        out["has_linked_tasks"] = False
    return out
