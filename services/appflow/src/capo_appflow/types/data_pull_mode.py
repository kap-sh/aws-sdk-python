"""Generated from Smithy shape ``com.amazonaws.appflow#DataPullMode``."""

from typing import Literal, TypeAlias, cast

DataPullMode: TypeAlias = Literal[
    "Incremental",
    "Complete",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataPullMode) -> str:
    return value


def deserialize_json(data: str) -> DataPullMode:
    return cast(DataPullMode, data)
