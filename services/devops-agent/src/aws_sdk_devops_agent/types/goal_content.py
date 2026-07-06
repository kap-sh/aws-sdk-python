"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalContent``."""

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError


class GoalContent(TypedDict, closed=True):
    description: "str"
    """<p>A detailed description of the goal.</p>"""
    objectives: "str"
    """<p>The objectives to be achieved for this goal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GoalContent) -> dict:
    out: dict = {}
    out["description"] = value["description"]
    out["objectives"] = value["objectives"]
    return out


def deserialize_json(data: dict) -> GoalContent:
    out: GoalContent = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("GoalContent.description required")
    if "objectives" in data:
        out["objectives"] = data["objectives"]
    else:
        raise DeserializationError("GoalContent.objectives required")
    return out
