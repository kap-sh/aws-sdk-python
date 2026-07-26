"""Generated from Smithy shape ``com.amazonaws.datazone#DataSourceRunType``."""

from typing import Literal, TypeAlias, cast

DataSourceRunType: TypeAlias = Literal[
    "PRIORITIZED",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceRunType) -> str:
    return value


def deserialize_json(data: str) -> DataSourceRunType:
    return cast(DataSourceRunType, data)
