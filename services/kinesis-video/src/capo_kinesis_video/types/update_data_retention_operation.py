"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateDataRetentionOperation``."""

from typing import Literal, TypeAlias, cast

UpdateDataRetentionOperation: TypeAlias = Literal[
    "INCREASE_DATA_RETENTION",
    "DECREASE_DATA_RETENTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataRetentionOperation) -> str:
    return value


def deserialize_json(data: str) -> UpdateDataRetentionOperation:
    return cast(UpdateDataRetentionOperation, data)
