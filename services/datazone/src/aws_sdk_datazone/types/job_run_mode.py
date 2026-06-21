"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunMode``."""

from typing import Literal, TypeAlias, cast

JobRunMode: TypeAlias = Literal[
    "SCHEDULED",
    "ON_DEMAND",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobRunMode) -> str:
    return value


def deserialize_json(data: str) -> JobRunMode:
    return cast(JobRunMode, data)
