"""Generated from Smithy shape ``com.amazonaws.guardduty#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

DataSourceStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceStatus:
    return cast(DataSourceStatus, data)
