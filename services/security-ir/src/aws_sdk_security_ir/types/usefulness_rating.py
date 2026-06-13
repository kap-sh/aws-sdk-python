"""Generated from Smithy shape ``com.amazonaws.securityir#UsefulnessRating``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_security_ir.errors import DeserializationError

UsefulnessRating: TypeAlias = Literal[
    "USEFUL",
    "NOT_USEFUL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USEFUL",
        "NOT_USEFUL",
    )
)


def serialize_json(value: UsefulnessRating) -> str:
    return value


def deserialize_json(data: str) -> UsefulnessRating:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UsefulnessRating value: {data!r}")
    return cast(UsefulnessRating, data)
