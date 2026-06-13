"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateBacklogTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.backlog_task_description
    import aws_sdk_devops_agent.types.backlog_task_title
    import aws_sdk_devops_agent.types.priority
    import aws_sdk_devops_agent.types.reference_input
    import aws_sdk_devops_agent.types.task_type


class CreateBacklogTaskRequest(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space where the task will be created</p>"""
    reference: NotRequired["aws_sdk_devops_agent.types.reference_input.ReferenceInput"]
    """<p>Optional reference information for the task</p>"""
    task_type: "aws_sdk_devops_agent.types.task_type.TaskType"
    """<p>The type of task being created</p>"""
    title: "aws_sdk_devops_agent.types.backlog_task_title.BacklogTaskTitle"
    """<p>The title of the backlog task</p>"""
    description: NotRequired[
        "aws_sdk_devops_agent.types.backlog_task_description.BacklogTaskDescription"
    ]
    """<p>Optional detailed description of the task</p>"""
    priority: "aws_sdk_devops_agent.types.priority.Priority"
    """<p>The priority level of the task</p>"""
    client_token: NotRequired["str"]
    """<p>Client-provided token for idempotent operations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBacklogTaskRequest) -> dict:
    out: dict = {}
    if "reference" in value:
        import aws_sdk_devops_agent.types.reference_input

        out["reference"] = aws_sdk_devops_agent.types.reference_input.serialize_json(
            value["reference"]
        )
    import aws_sdk_devops_agent.types.task_type

    out["taskType"] = aws_sdk_devops_agent.types.task_type.serialize_json(
        value["task_type"]
    )
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_devops_agent.types.priority

    out["priority"] = aws_sdk_devops_agent.types.priority.serialize_json(
        value["priority"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateBacklogTaskRequest:
    out: CreateBacklogTaskRequest = {}  # type: ignore[typeddict-item]
    if "reference" in data:
        import aws_sdk_devops_agent.types.reference_input

        out["reference"] = aws_sdk_devops_agent.types.reference_input.deserialize_json(
            data["reference"]
        )
    if "taskType" in data:
        import aws_sdk_devops_agent.types.task_type

        out["task_type"] = aws_sdk_devops_agent.types.task_type.deserialize_json(
            data["taskType"]
        )
    else:
        raise DeserializationError("CreateBacklogTaskRequest.task_type required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("CreateBacklogTaskRequest.title required")
    if "description" in data:
        out["description"] = data["description"]
    if "priority" in data:
        import aws_sdk_devops_agent.types.priority

        out["priority"] = aws_sdk_devops_agent.types.priority.deserialize_json(
            data["priority"]
        )
    else:
        raise DeserializationError("CreateBacklogTaskRequest.priority required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
