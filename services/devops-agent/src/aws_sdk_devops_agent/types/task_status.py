"""Generated from Smithy shape ``com.amazonaws.devopsagent#TaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStatus value: {data!r}")
    return cast(TaskStatus, data)
