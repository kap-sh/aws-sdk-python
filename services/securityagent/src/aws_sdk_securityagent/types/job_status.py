"""Generated from Smithy shape ``com.amazonaws.securityagent#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Status of a pentest job.</p>"""
JobStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "STOPPING",
    "STOPPED",
    "FAILED",
    "COMPLETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "STOPPING",
        "STOPPED",
        "FAILED",
        "COMPLETED",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
