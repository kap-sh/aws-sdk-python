"""Generated from Smithy shape ``com.amazonaws.macie2#IsMonitoredByJob``."""

from typing import Literal, TypeAlias, cast

IsMonitoredByJob: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: IsMonitoredByJob) -> str:
    return value


def deserialize_json(data: str) -> IsMonitoredByJob:
    return cast(IsMonitoredByJob, data)
