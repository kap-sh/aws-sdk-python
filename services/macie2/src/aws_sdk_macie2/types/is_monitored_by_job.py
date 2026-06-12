"""Generated from Smithy shape ``com.amazonaws.macie2#IsMonitoredByJob``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

IsMonitoredByJob: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
        "UNKNOWN",
    )
)


def serialize_json(value: IsMonitoredByJob) -> str:
    return value


def deserialize_json(data: str) -> IsMonitoredByJob:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsMonitoredByJob value: {data!r}")
    return cast(IsMonitoredByJob, data)
