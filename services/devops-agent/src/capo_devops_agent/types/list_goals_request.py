"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListGoalsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.goal_status
    import capo_devops_agent.types.goal_type
    import capo_devops_agent.types.next_token


class ListGoalsRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space</p>"""
    status: NotRequired["capo_devops_agent.types.goal_status.GoalStatus"]
    """<p>Filter goals by goal status</p>"""
    goal_type: NotRequired["capo_devops_agent.types.goal_type.GoalType"]
    """<p>Filter goals by goal type</p>"""
    limit: "int"
    """<p>Maximum number of goals to return</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token for the next set of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGoalsRequest) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_devops_agent.types.goal_status

        out["status"] = capo_devops_agent.types.goal_status.serialize_json(
            value["status"]
        )
    if "goal_type" in value:
        import capo_devops_agent.types.goal_type

        out["goalType"] = capo_devops_agent.types.goal_type.serialize_json(
            value["goal_type"]
        )
    out["limit"] = value.get("limit", 50)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGoalsRequest:
    out: ListGoalsRequest = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_devops_agent.types.goal_status

        out["status"] = capo_devops_agent.types.goal_status.deserialize_json(
            data["status"]
        )
    if "goalType" in data:
        import capo_devops_agent.types.goal_type

        out["goal_type"] = capo_devops_agent.types.goal_type.deserialize_json(
            data["goalType"]
        )
    if "limit" in data:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 50
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
