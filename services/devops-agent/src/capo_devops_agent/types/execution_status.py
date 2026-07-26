"""Generated from Smithy shape ``com.amazonaws.devopsagent#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Possible states of an execution</p>"""
ExecutionStatus: TypeAlias = Literal[
    "FAILED",
    "RUNNING",
    "STOPPED",
    "CANCELED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ExecutionStatus:
    return cast(ExecutionStatus, data)
