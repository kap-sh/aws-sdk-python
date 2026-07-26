"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataSourceStatus``."""

from typing import Literal, TypeAlias, cast

DataSourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETING",
    "DELETE_UNSUCCESSFUL",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceStatus) -> str:
    return value


def deserialize_json(data: str) -> DataSourceStatus:
    return cast(DataSourceStatus, data)
