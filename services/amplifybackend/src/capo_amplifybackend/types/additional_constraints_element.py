"""Generated from Smithy shape ``com.amazonaws.amplifybackend#AdditionalConstraintsElement``."""

from typing import Literal, TypeAlias, cast

AdditionalConstraintsElement: TypeAlias = Literal[
    "REQUIRE_DIGIT",
    "REQUIRE_LOWERCASE",
    "REQUIRE_SYMBOL",
    "REQUIRE_UPPERCASE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalConstraintsElement) -> str:
    return value


def deserialize_json(data: str) -> AdditionalConstraintsElement:
    return cast(AdditionalConstraintsElement, data)
