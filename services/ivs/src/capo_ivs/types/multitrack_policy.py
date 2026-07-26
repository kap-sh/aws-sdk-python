"""Generated from Smithy shape ``com.amazonaws.ivs#MultitrackPolicy``."""

from typing import Literal, TypeAlias, cast

MultitrackPolicy: TypeAlias = Literal[
    "ALLOW",
    "REQUIRE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MultitrackPolicy) -> str:
    return value


def deserialize_json(data: str) -> MultitrackPolicy:
    return cast(MultitrackPolicy, data)
