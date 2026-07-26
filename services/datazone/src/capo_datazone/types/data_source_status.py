"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

DataSourceStatus: TypeAlias = Literal[
    "CREATING",
    "FAILED_CREATION",
    "READY",
    "UPDATING",
    "FAILED_UPDATE",
    "RUNNING",
    "DELETING",
    "FAILED_DELETION",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceStatus:
    return cast(DataSourceStatus, data)
