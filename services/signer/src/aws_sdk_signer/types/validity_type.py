"""Generated from Smithy shape ``com.amazonaws.signer#ValidityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_signer.errors import DeserializationError

ValidityType: TypeAlias = Literal[
    "DAYS",
    "MONTHS",
    "YEARS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAYS",
        "MONTHS",
        "YEARS",
    )
)


def serialize_json(value: ValidityType) -> str:
    return value


def deserialize_json(data: str) -> ValidityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidityType value: {data!r}")
    return cast(ValidityType, data)
