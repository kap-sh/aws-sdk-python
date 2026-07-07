"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalScheduleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.scheduler_state


class GoalScheduleInput(TypedDict, closed=True):
    state: "aws_sdk_devops_agent.types.scheduler_state.SchedulerState"
    """<p>Whether the schedule is enabled or disabled</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GoalScheduleInput) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.scheduler_state

    out["state"] = aws_sdk_devops_agent.types.scheduler_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> GoalScheduleInput:
    out: GoalScheduleInput = {}  # type: ignore[typeddict-item]
    if "state" in data:
        import aws_sdk_devops_agent.types.scheduler_state

        out["state"] = aws_sdk_devops_agent.types.scheduler_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("GoalScheduleInput.state required")
    return out
