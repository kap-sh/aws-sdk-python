"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListGoalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.goal_list


class ListGoalsResponse(TypedDict, closed=True):
    goals: "aws_sdk_devops_agent.types.goal_list.GoalList"
    """<p>List of goals matching the criteria</p>"""
    next_token: NotRequired["str"]
    """<p>Pagination token for the next set of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGoalsResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.goal_list

    out["goals"] = aws_sdk_devops_agent.types.goal_list.serialize_json(value["goals"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGoalsResponse:
    out: ListGoalsResponse = {}  # type: ignore[typeddict-item]
    if "goals" in data:
        import aws_sdk_devops_agent.types.goal_list

        out["goals"] = aws_sdk_devops_agent.types.goal_list.deserialize_json(
            data["goals"]
        )
    else:
        raise DeserializationError("ListGoalsResponse.goals required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
