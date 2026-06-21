"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceErrorInfoType``."""

from typing import Literal, TypeAlias, cast

DataSourceErrorInfoType: TypeAlias = Literal[
    "ACCESS_DENIED",
    "COPY_SOURCE_NOT_FOUND",
    "TIMEOUT",
    "ENGINE_VERSION_NOT_SUPPORTED",
    "UNKNOWN_HOST",
    "GENERIC_SQL_FAILURE",
    "CONFLICT",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceErrorInfoType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceErrorInfoType:
    return cast(DataSourceErrorInfoType, data)
