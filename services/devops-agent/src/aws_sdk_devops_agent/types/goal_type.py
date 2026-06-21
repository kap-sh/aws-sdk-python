"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalType``."""

from typing import Literal, TypeAlias, cast

"""<p>Type of goal based on its origin</p>"""
GoalType: TypeAlias = Literal[
    "CUSTOMER_DEFINED",
    "ONCALL_REPORT",
]


# --- restJson1 ser/de ---
def serialize_json(value: GoalType) -> str:
    return value


def deserialize_json(data: str) -> GoalType:
    return cast(GoalType, data)
