"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlsUpdatable``."""

from typing import Literal, TypeAlias, cast

StandardsControlsUpdatable: TypeAlias = Literal[
    "READY_FOR_UPDATES",
    "NOT_READY_FOR_UPDATES",
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlsUpdatable) -> str:
    return value


def deserialize_json(data: str) -> StandardsControlsUpdatable:
    return cast(StandardsControlsUpdatable, data)
