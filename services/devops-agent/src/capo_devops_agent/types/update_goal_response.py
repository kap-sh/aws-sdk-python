"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateGoalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.goal


class UpdateGoalResponse(TypedDict, closed=True):
    goal: "capo_devops_agent.types.goal.Goal"
    """<p>The updated goal object</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGoalResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.goal

    out["goal"] = capo_devops_agent.types.goal.serialize_json(value["goal"])
    return out


def deserialize_json(data: dict) -> UpdateGoalResponse:
    out: UpdateGoalResponse = {}  # type: ignore[typeddict-item]
    if "goal" in data:
        import capo_devops_agent.types.goal

        out["goal"] = capo_devops_agent.types.goal.deserialize_json(data["goal"])
    else:
        raise DeserializationError("UpdateGoalResponse.goal required")
    return out
