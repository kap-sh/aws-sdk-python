"""Generated from Smithy shape ``com.amazonaws.quicksight#CommitMode``."""

from typing import Literal, TypeAlias, cast

CommitMode: TypeAlias = Literal[
    "AUTO",
    "MANUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: CommitMode) -> str:
    return value


def deserialize_json(data: str) -> CommitMode:
    return cast(CommitMode, data)
