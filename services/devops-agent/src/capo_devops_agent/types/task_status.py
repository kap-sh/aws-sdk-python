"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Possible states of a task throughout its lifecycle</p>"""
TaskStatus: TypeAlias = Literal[
    "PENDING_TRIAGE",
    "LINKED",
    "PENDING_START",
    "IN_PROGRESS",
    "PENDING_CUSTOMER_APPROVAL",
    "COMPLETED",
    "FAILED",
    "TIMED_OUT",
    "CANCELED",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    return cast(TaskStatus, data)
