"""Generated from Smithy shape ``com.amazonaws.medicalimaging#Operator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medical_imaging.errors import DeserializationError

Operator: TypeAlias = Literal[
    "EQUAL",
    "BETWEEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUAL",
        "BETWEEN",
    )
)


def serialize_json(value: Operator) -> str:
    return value


def deserialize_json(data: str) -> Operator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Operator value: {data!r}")
    return cast(Operator, data)
