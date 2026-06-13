"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Possible states of a goal throughout its lifecycle</p>"""
GoalStatus: TypeAlias = Literal[
    "ACTIVE",
    "PAUSED",
    "COMPLETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PAUSED",
        "COMPLETE",
    )
)


def serialize_json(value: GoalStatus) -> str:
    return value


def deserialize_json(data: str) -> GoalStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GoalStatus value: {data!r}")
    return cast(GoalStatus, data)
