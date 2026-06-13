"""Generated from Smithy shape ``com.amazonaws.devopsagent#GoalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Type of goal based on its origin</p>"""
GoalType: TypeAlias = Literal[
    "CUSTOMER_DEFINED",
    "ONCALL_REPORT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_DEFINED",
        "ONCALL_REPORT",
    )
)


def serialize_json(value: GoalType) -> str:
    return value


def deserialize_json(data: str) -> GoalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GoalType value: {data!r}")
    return cast(GoalType, data)
