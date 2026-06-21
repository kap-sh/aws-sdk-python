"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BatchEntryCompletionStatus``."""

from typing import Literal, TypeAlias, cast

BatchEntryCompletionStatus: TypeAlias = Literal[
    "SUCCESS",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchEntryCompletionStatus) -> str:
    return value


def deserialize_json(data: str) -> BatchEntryCompletionStatus:
    return cast(BatchEntryCompletionStatus, data)
