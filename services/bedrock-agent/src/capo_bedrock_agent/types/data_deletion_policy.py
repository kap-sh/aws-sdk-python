"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DataDeletionPolicy``."""

from typing import Literal, TypeAlias, cast

DataDeletionPolicy: TypeAlias = Literal[
    "RETAIN",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataDeletionPolicy) -> str:
    return value


def deserialize_json(data: str) -> DataDeletionPolicy:
    return cast(DataDeletionPolicy, data)
