"""Generated from Smithy shape ``com.amazonaws.deadline#TagPropagationMode``."""

from typing import Literal, TypeAlias, cast

TagPropagationMode: TypeAlias = Literal[
    "NO_PROPAGATION",
    "PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH",
]


# --- restJson1 ser/de ---
def serialize_json(value: TagPropagationMode) -> str:
    return value


def deserialize_json(data: str) -> TagPropagationMode:
    return cast(TagPropagationMode, data)
