"""Generated from Smithy shape ``com.amazonaws.amplifybackend#AdditionalConstraintsElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

AdditionalConstraintsElement: TypeAlias = Literal[
    "REQUIRE_DIGIT",
    "REQUIRE_LOWERCASE",
    "REQUIRE_SYMBOL",
    "REQUIRE_UPPERCASE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUIRE_DIGIT",
        "REQUIRE_LOWERCASE",
        "REQUIRE_SYMBOL",
        "REQUIRE_UPPERCASE",
    )
)


def serialize_json(value: AdditionalConstraintsElement) -> str:
    return value


def deserialize_json(data: str) -> AdditionalConstraintsElement:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AdditionalConstraintsElement value: {data!r}"
        )
    return cast(AdditionalConstraintsElement, data)
