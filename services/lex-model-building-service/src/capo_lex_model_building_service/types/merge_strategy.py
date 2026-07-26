"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#MergeStrategy``."""

from typing import Literal, TypeAlias, cast

MergeStrategy: TypeAlias = Literal[
    "OVERWRITE_LATEST",
    "FAIL_ON_CONFLICT",
]


# --- restJson1 ser/de ---
def serialize_json(value: MergeStrategy) -> str:
    return value


def deserialize_json(data: str) -> MergeStrategy:
    return cast(MergeStrategy, data)
