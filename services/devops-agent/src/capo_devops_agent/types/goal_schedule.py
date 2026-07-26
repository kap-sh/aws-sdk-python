"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.scheduler_state


class GoalSchedule(TypedDict, closed=True):
    state: "capo_devops_agent.types.scheduler_state.SchedulerState"
    """<p>Whether the schedule is enabled or disabled</p>"""
    expression: NotRequired["str"]
    """<p>Schedule expression (e.g., 'rate(7 days)')</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GoalSchedule) -> dict:
    out: dict = {}
    import capo_devops_agent.types.scheduler_state

    out["state"] = capo_devops_agent.types.scheduler_state.serialize_json(
        value["state"]
    )
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> GoalSchedule:
    out: GoalSchedule = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import capo_devops_agent.types.scheduler_state

        out["state"] = capo_devops_agent.types.scheduler_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("GoalSchedule.state required")
    if "expression" in data:
        out["expression"] = data["expression"]
    return out
