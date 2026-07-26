"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateGoalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.goal_schedule_input


class UpdateGoalRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier for the agent space containing the goal</p>"""
    goal_id: "str"
    """<p>The unique identifier of the goal to update</p>"""
    evaluation_schedule: NotRequired[
        "capo_devops_agent.types.goal_schedule_input.GoalScheduleInput"
    ]
    """<p>Update goal schedule state</p>"""
    client_token: NotRequired["str"]
    """<p>Client-provided token for idempotent operations</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGoalRequest) -> dict:
    out: dict = {}
    if "evaluation_schedule" in value:
        import capo_devops_agent.types.goal_schedule_input

        out["evaluationSchedule"] = (
            capo_devops_agent.types.goal_schedule_input.serialize_json(
                value["evaluation_schedule"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateGoalRequest:
    out: UpdateGoalRequest = {}  # type: ignore[typeddict-item]
    if "evaluationSchedule" in data:
        import capo_devops_agent.types.goal_schedule_input

        out["evaluation_schedule"] = (
            capo_devops_agent.types.goal_schedule_input.deserialize_json(
                data["evaluationSchedule"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
