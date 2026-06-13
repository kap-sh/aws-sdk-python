"""Generated from Smithy shape ``com.amazonaws.devopsagent#Recommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.back_log_timestamp
    import aws_sdk_devops_agent.types.recommendation_content
    import aws_sdk_devops_agent.types.recommendation_priority
    import aws_sdk_devops_agent.types.recommendation_status


class Recommendation(TypedDict):
    agent_space_arn: "str"
    """<p>ARN of the agent space this recommendation belongs to</p>"""
    recommendation_id: "str"
    """<p>The unique identifier for this recommendation</p>"""
    task_id: "str"
    """<p>ID of the task that generated the recommendation</p>"""
    goal_id: NotRequired["str"]
    """<p>ID of the goal this recommendation is associated with</p>"""
    title: "str"
    """<p>The title of the recommendation</p>"""
    content: "aws_sdk_devops_agent.types.recommendation_content.RecommendationContent"
    """<p>Content of the recommendation</p>"""
    status: "aws_sdk_devops_agent.types.recommendation_status.RecommendationStatus"
    """<p>Current status of the recommendation</p>"""
    priority: (
        "aws_sdk_devops_agent.types.recommendation_priority.RecommendationPriority"
    )
    """<p>Priority level of the recommendation</p>"""
    goal_version: NotRequired["int"]
    """<p>Version of the goal at the time this recommendation was generated</p>"""
    additional_context: NotRequired["str"]
    """<p>Additional context for recommendation</p>"""
    rank_position: NotRequired["int"]
    """<p>Position in ranked list (1 = highest priority)</p>"""
    ranked_at: NotRequired[
        "aws_sdk_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    ]
    """<p>Timestamp when the recommendation was last ranked</p>"""
    created_at: "aws_sdk_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this recommendation was created</p>"""
    updated_at: "aws_sdk_devops_agent.types.back_log_timestamp.BackLogTimestamp"
    """<p>Timestamp when this recommendation was last updated</p>"""
    version: "int"
    """<p>Version number for optimistic locking</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    out["agentSpaceArn"] = value["agent_space_arn"]
    out["recommendationId"] = value["recommendation_id"]
    out["taskId"] = value["task_id"]
    if "goal_id" in value:
        out["goalId"] = value["goal_id"]
    out["title"] = value["title"]
    import aws_sdk_devops_agent.types.recommendation_content

    out["content"] = aws_sdk_devops_agent.types.recommendation_content.serialize_json(
        value["content"]
    )
    import aws_sdk_devops_agent.types.recommendation_status

    out["status"] = aws_sdk_devops_agent.types.recommendation_status.serialize_json(
        value["status"]
    )
    import aws_sdk_devops_agent.types.recommendation_priority

    out["priority"] = aws_sdk_devops_agent.types.recommendation_priority.serialize_json(
        value["priority"]
    )
    if "goal_version" in value:
        out["goalVersion"] = value["goal_version"]
    if "additional_context" in value:
        out["additionalContext"] = value["additional_context"]
    if "rank_position" in value:
        out["rankPosition"] = value["rank_position"]
    if "ranked_at" in value:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["rankedAt"] = aws_sdk_devops_agent.types.back_log_timestamp.serialize_json(
            value["ranked_at"]
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
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "agentSpaceArn" in data:
        out["agent_space_arn"] = data["agentSpaceArn"]
    else:
        raise DeserializationError("Recommendation.agent_space_arn required")
    if "recommendationId" in data:
        out["recommendation_id"] = data["recommendationId"]
    else:
        raise DeserializationError("Recommendation.recommendation_id required")
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("Recommendation.task_id required")
    if "goalId" in data:
        out["goal_id"] = data["goalId"]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("Recommendation.title required")
    if "content" in data:
        import aws_sdk_devops_agent.types.recommendation_content

        out["content"] = (
            aws_sdk_devops_agent.types.recommendation_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("Recommendation.content required")
    if "status" in data:
        import aws_sdk_devops_agent.types.recommendation_status

        out["status"] = (
            aws_sdk_devops_agent.types.recommendation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("Recommendation.status required")
    if "priority" in data:
        import aws_sdk_devops_agent.types.recommendation_priority

        out["priority"] = (
            aws_sdk_devops_agent.types.recommendation_priority.deserialize_json(
                data["priority"]
            )
        )
    else:
        raise DeserializationError("Recommendation.priority required")
    if "goalVersion" in data:
        out["goal_version"] = data["goalVersion"]
    if "additionalContext" in data:
        out["additional_context"] = data["additionalContext"]
    if "rankPosition" in data:
        out["rank_position"] = data["rankPosition"]
    if "rankedAt" in data:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["ranked_at"] = (
            aws_sdk_devops_agent.types.back_log_timestamp.deserialize_json(
                data["rankedAt"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["created_at"] = (
            aws_sdk_devops_agent.types.back_log_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Recommendation.created_at required")
    if "updatedAt" in data:
        import aws_sdk_devops_agent.types.back_log_timestamp

        out["updated_at"] = (
            aws_sdk_devops_agent.types.back_log_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Recommendation.updated_at required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("Recommendation.version required")
    return out
