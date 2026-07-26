"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#MergeStrategy``."""

from typing import Literal, TypeAlias, cast

MergeStrategy: TypeAlias = Literal[
    "Overwrite",
    "FailOnConflict",
    "Append",
]


# --- restJson1 ser/de ---
def serialize_json(value: MergeStrategy) -> str:
    return value


def deserialize_json(data: str) -> MergeStrategy:
    return cast(MergeStrategy, data)
