"""Generated from Smithy shape ``com.amazonaws.devopsagent#SchedulerState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>State of Goal Schedule. Mirrors EventBridge Scheduler State</p>"""
SchedulerState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: SchedulerState) -> str:
    return value


def deserialize_json(data: str) -> SchedulerState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SchedulerState value: {data!r}")
    return cast(SchedulerState, data)
