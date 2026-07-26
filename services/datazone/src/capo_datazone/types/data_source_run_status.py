"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunStatus``."""

from typing import Literal, TypeAlias, cast

DataSourceRunStatus: TypeAlias = Literal[
    "REQUESTED",
    "RUNNING",
    "FAILED",
    "PARTIALLY_SUCCEEDED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceRunStatus:
    return cast(DataSourceRunStatus, data)
