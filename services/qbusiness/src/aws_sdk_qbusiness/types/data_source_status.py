"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

DataSourceStatus: TypeAlias = Literal[
    "PENDING_CREATION",
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceStatus:
    return cast(DataSourceStatus, data)
