"""Generated from Smithy shape ``com.amazonaws.ivs#MultitrackPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs.errors import DeserializationError

MultitrackPolicy: TypeAlias = Literal[
    "ALLOW",
    "REQUIRE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "REQUIRE",
    )
)


def serialize_json(value: MultitrackPolicy) -> str:
    return value


def deserialize_json(data: str) -> MultitrackPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MultitrackPolicy value: {data!r}")
    return cast(MultitrackPolicy, data)
