"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Possible states of a goal throughout its lifecycle</p>"""
GoalStatus: TypeAlias = Literal[
    "ACTIVE",
    "PAUSED",
    "COMPLETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: GoalStatus) -> str:
    return value


def deserialize_json(data: str) -> GoalStatus:
    return cast(GoalStatus, data)
