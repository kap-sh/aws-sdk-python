"""Generated from Smithy shape ``com.amazonaws.securityhub#RecordState``."""

from typing import Literal, TypeAlias, cast

RecordState: TypeAlias = Literal[
    "ACTIVE",
    "ARCHIVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordState) -> str:
    return value


def deserialize_json(data: str) -> RecordState:
    return cast(RecordState, data)
