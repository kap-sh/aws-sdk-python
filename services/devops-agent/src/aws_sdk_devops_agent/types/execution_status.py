"""Generated from Smithy shape ``com.amazonaws.devopsagent#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Possible states of an execution</p>"""
ExecutionStatus: TypeAlias = Literal[
    "FAILED",
    "RUNNING",
    "STOPPED",
    "CANCELED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAILED",
        "RUNNING",
        "STOPPED",
        "CANCELED",
        "TIMED_OUT",
    )
)


def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {data!r}")
    return cast(ExecutionStatus, data)
