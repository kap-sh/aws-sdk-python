"""Generated from Smithy shape ``com.amazonaws.devopsagent#SchedulerState``."""

from typing import Literal, TypeAlias, cast

"""<p>State of Goal Schedule. Mirrors EventBridge Scheduler State</p>"""
SchedulerState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SchedulerState) -> str:
    return value


def deserialize_json(data: str) -> SchedulerState:
    return cast(SchedulerState, data)
