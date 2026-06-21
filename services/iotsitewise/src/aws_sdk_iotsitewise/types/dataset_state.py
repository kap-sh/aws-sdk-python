"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetState``."""

from typing import Literal, TypeAlias, cast

DatasetState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetState) -> str:
    return value


def deserialize_json(data: str) -> DatasetState:
    return cast(DatasetState, data)
