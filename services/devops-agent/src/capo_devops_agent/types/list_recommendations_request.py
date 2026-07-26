"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.recommendation_priority
    import capo_devops_agent.types.recommendation_status
    import capo_devops_agent.types.resource_id


class ListRecommendationsRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the recommendations</p>"""
    task_id: NotRequired["capo_devops_agent.types.resource_id.ResourceId"]
    """<p>Optional task ID to filter recommendations by specific task</p>"""
    goal_id: NotRequired["capo_devops_agent.types.resource_id.ResourceId"]
    """<p>Optional goal ID to filter recommendations by specific goal</p>"""
    status: NotRequired[
        "capo_devops_agent.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Optional status to filter recommendations by their current status</p>"""
    priority: NotRequired[
        "capo_devops_agent.types.recommendation_priority.RecommendationPriority"
    ]
    """<p>Optional priority to filter recommendations by priority level</p>"""
    limit: "int"
    """<p>Maximum number of recommendations to return in a single response</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsRequest) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "goal_id" in value:
        out["goalId"] = value["goal_id"]
    if "status" in value:
        import capo_devops_agent.types.recommendation_status

        out["status"] = capo_devops_agent.types.recommendation_status.serialize_json(
            value["status"]
        )
    if "priority" in value:
        import capo_devops_agent.types.recommendation_priority

        out["priority"] = (
            capo_devops_agent.types.recommendation_priority.serialize_json(
                value["priority"]
            )
        )
    out["limit"] = value.get("limit", 50)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommendationsRequest:
    out: ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "goalId" in data:
        out["goal_id"] = data["goalId"]
    if "status" in data:
        import capo_devops_agent.types.recommendation_status

        out["status"] = capo_devops_agent.types.recommendation_status.deserialize_json(
            data["status"]
        )
    if "priority" in data:
        import capo_devops_agent.types.recommendation_priority

        out["priority"] = (
            capo_devops_agent.types.recommendation_priority.deserialize_json(
                data["priority"]
            )
        )
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 50
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
