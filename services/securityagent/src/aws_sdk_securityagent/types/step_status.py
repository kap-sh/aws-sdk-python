"""Generated from Smithy shape ``com.amazonaws.securityagent#StepStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Pentest job step status.</p>"""
StepStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "STOPPED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "STOPPED",
    )
)


def serialize_json(value: StepStatus) -> str:
    return value


def deserialize_json(data: str) -> StepStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepStatus value: {data!r}")
    return cast(StepStatus, data)
