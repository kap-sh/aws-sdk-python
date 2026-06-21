"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceErrorType``."""

from typing import Literal, TypeAlias, cast

DataSourceErrorType: TypeAlias = Literal[
    "ACCESS_DENIED_EXCEPTION",
    "CONFLICT_EXCEPTION",
    "INTERNAL_SERVER_EXCEPTION",
    "RESOURCE_NOT_FOUND_EXCEPTION",
    "SERVICE_QUOTA_EXCEEDED_EXCEPTION",
    "THROTTLING_EXCEPTION",
    "VALIDATION_EXCEPTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceErrorType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceErrorType:
    return cast(DataSourceErrorType, data)
