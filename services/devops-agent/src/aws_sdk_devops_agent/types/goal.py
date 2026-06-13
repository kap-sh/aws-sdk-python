"""Generated from Smithy shape ``com.amazonaws.devopsagent#Goal``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.back_log_timestamp
    import aws_sdk_devops_agent.types.goal_content
    import aws_sdk_devops_agent.types.goal_schedule
    import aws_sdk_devops_agent.types.goal_status
    import aws_sdk_devops_agent.types.goal_type


class Goal(TypedDict):
    agent_space_arn: "str"
    """<p>The unique identifier for the agent space containing this goal</p>"""
    goal_id: "str"
    """<p>The unique identifier for this goal</p>"""
    title: "str"
    """<p>The title of the goal</p>"""
    content: "aws_sdk_devops_agent.types.goal_content.GoalContent"
    """<p>Content of the goal</p>"""
    status: "aws_sdk_devops_agent.types.goal_status.GoalStatus"
    """<p>Current status of the goal itself</p>"""
    goal_type: "aws_sdk_devops_agent.types.goal_type.GoalType"
    """<p>Type of goal based on its origin</p>"""
    created_at: "aws_sdk_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this goal was created</p>"""
    updated_at: "aws_sdk_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this goal was last updated</p>"""
    last_evaluated_at: NotRequired[
        "aws_sdk_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    ]
    """<p>Timestamp when the goal was last evaluated</p>"""
    last_task_id: NotRequired["str"]
    """<p>ID of the most recent task associated with this goal</p>"""
    last_successful_task_id: NotRequired["str"]
    """<p>ID of the most recent successful task associated with this goal</p>"""
    version: "int"
    """<p>Version number for optimistic locking</p>"""
    evaluation_schedule: NotRequired[
        "aws_sdk_devops_agent.types.goal_schedule.GoalSchedule"
    ]
    """<p>Goal Schedule. Allows to schedule the goal to run periodically, as well as disable a goal temporarily</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Goal) -> dict:
    out: dict = {}
    out["agentSpaceArn"] = value["agent_space_arn"]
    out["goalId"] = value["goal_id"]
    out["title"] = value["title"]
    import aws_sdk_devops_agent.types.goal_content

    out["content"] = aws_sdk_devops_agent.types.goal_content.serialize_json(
        value["content"]
    )
    import aws_sdk_devops_agent.types.goal_status

    out["status"] = aws_sdk_devops_agent.types.goal_status.serialize_json(
        value["status"]
    )
    import aws_sdk_devops_agent.types.goal_type

    out["goalType"] = aws_sdk_devops_agent.types.goal_type.serialize_json(
        value.get("goal_type", "ONCALL_REPORT")
    )
    import aws_sdk_devops_agent.types.back_log_timestamp

    out["createdAt"] = aws_sdk_devops_agent.types.back_log_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_devops_agent.types.back_log_timestamp

    out["updatedAt"] = aws_sdk_devops_agent.types.back_log_timestamp.serialize_json(
        value["updated_at"]
    )
    if "last_evaluated_at" in value:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["lastEvaluatedAt"] = (
            aws_sdk_devops_agent.types.back_log_timestamp.serialize_json(
                value["last_evaluated_at"]
            )
        )
    if "last_task_id" in value:
        out["lastTaskId"] = value["last_task_id"]
    if "last_successful_task_id" in value:
        out["lastSuccessfulTaskId"] = value["last_successful_task_id"]
    out["version"] = value["version"]
    if "evaluation_schedule" in value:
        import aws_sdk_devops_agent.types.goal_schedule

        out["evaluationSchedule"] = (
            aws_sdk_devops_agent.types.goal_schedule.serialize_json(
                value["evaluation_schedule"]
            )
        )
    return out


def deserialize_json(data: dict) -> Goal:
    out: Goal = {}  # type: ignore[typeddict-item]
    if "agentSpaceArn" in data:
        out["agent_space_arn"] = data["agentSpaceArn"]
    else:
        raise DeserializationError("Goal.agent_space_arn required")
    if "goalId" in data:
        out["goal_id"] = data["goalId"]
    else:
        raise DeserializationError("Goal.goal_id required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("Goal.title required")
    if "content" in data:
        import aws_sdk_devops_agent.types.goal_content

        out["content"] = aws_sdk_devops_agent.types.goal_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("Goal.content required")
    if "status" in data:
        import aws_sdk_devops_agent.types.goal_status

        out["status"] = aws_sdk_devops_agent.types.goal_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("Goal.status required")
    if "goalType" in data:
        import aws_sdk_devops_agent.types.goal_type

        out["goal_type"] = aws_sdk_devops_agent.types.goal_type.deserialize_json(
            data["goalType"]
        )
    else:
        out["goal_type"] = "ONCALL_REPORT"
    if "createdAt" in data:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types.back_log_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Goal.created_at required")
    if "updatedAt" in data:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["updated_at"] = (
            aws_sdk_devops_agent.types.back_log_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Goal.updated_at required")
    if "lastEvaluatedAt" in data:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["last_evaluated_at"] = (
            aws_sdk_devops_agent.types.back_log_timestamp.deserialize_json(
                data["lastEvaluatedAt"]
            )
        )
    if "lastTaskId" in data:
        out["last_task_id"] = data["lastTaskId"]
    if "lastSuccessfulTaskId" in data:
        out["last_successful_task_id"] = data["lastSuccessfulTaskId"]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("Goal.version required")
    if "evaluationSchedule" in data:
        import aws_sdk_devops_agent.types.goal_schedule

        out["evaluation_schedule"] = (
            aws_sdk_devops_agent.types.goal_schedule.deserialize_json(
                data["evaluationSchedule"]
            )
        )
    return out
