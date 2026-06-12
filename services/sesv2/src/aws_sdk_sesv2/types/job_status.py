"""Generated from Smithy shape ``com.amazonaws.sesv2#JobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The status of a job.</p> <ul> <li> <p> <code>CREATED</code> – Job has just been created.</p> </li> <li> <p> <code>PROCESSING</code> – Job is processing.</p> </li> <li> <p> <code>ERROR</code> – An error occurred during processing.</p> </li> <li> <p> <code>COMPLETED</code> – Job has completed processing successfully.</p> </li> </ul>"""
JobStatus: TypeAlias = Literal[
    "CREATED",
    "PROCESSING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "PROCESSING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
    )
)


def serialize_json(value: JobStatus) -> str:
    return value


def deserialize_json(data: str) -> JobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobStatus value: {data!r}")
    return cast(JobStatus, data)
