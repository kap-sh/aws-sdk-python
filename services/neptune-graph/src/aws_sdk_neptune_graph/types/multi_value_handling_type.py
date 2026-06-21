"""Generated from Smithy shape ``com.amazonaws.neptunegraph#MultiValueHandlingType``."""

from typing import Literal, TypeAlias, cast

MultiValueHandlingType: TypeAlias = Literal[
    "TO_LIST",
    "PICK_FIRST",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiValueHandlingType) -> str:
    return value


def deserialize_json(data: str) -> MultiValueHandlingType:
    return cast(MultiValueHandlingType, data)
