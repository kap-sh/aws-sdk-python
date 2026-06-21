"""Generated from Smithy shape ``com.amazonaws.databrew#SampleType``."""

from typing import Literal, TypeAlias, cast

SampleType: TypeAlias = Literal[
    "FIRST_N",
    "LAST_N",
    "RANDOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: SampleType) -> str:
    return value


def deserialize_json(data: str) -> SampleType:
    return cast(SampleType, data)
