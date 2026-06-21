"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RangeMode``."""

from typing import Literal, TypeAlias, cast

RangeMode: TypeAlias = Literal[
    "FIRST",
    "LAST",
    "LAST_BEFORE_MISSING_VALUES",
    "INCLUSIVE",
    "EXCLUSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RangeMode) -> str:
    return value


def deserialize_json(data: str) -> RangeMode:
    return cast(RangeMode, data)
