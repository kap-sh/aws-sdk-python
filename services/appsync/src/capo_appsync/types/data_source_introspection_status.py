"""Generated from Smithy shape ``com.amazonaws.appsync#DataSourceIntrospectionStatus``."""

from typing import Literal, TypeAlias, cast

DataSourceIntrospectionStatus: TypeAlias = Literal[
    "PROCESSING",
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceIntrospectionStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceIntrospectionStatus:
    return cast(DataSourceIntrospectionStatus, data)
