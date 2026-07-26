"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ProcessBehavior``."""

from typing import Literal, TypeAlias, cast

ProcessBehavior: TypeAlias = Literal[
    "SAVE",
    "BUILD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProcessBehavior) -> str:
    return value


def deserialize_json(data: str) -> ProcessBehavior:
    return cast(ProcessBehavior, data)
