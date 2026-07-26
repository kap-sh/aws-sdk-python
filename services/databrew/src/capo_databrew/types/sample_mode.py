"""Generated from Smithy shape ``com.amazonaws.databrew#SampleMode``."""

from typing import Literal, TypeAlias, cast

SampleMode: TypeAlias = Literal[
    "FULL_DATASET",
    "CUSTOM_ROWS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SampleMode) -> str:
    return value


def deserialize_json(data: str) -> SampleMode:
    return cast(SampleMode, data)
