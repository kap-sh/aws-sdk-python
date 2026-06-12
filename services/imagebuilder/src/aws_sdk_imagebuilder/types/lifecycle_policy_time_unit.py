"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyTimeUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_imagebuilder.errors import DeserializationError

LifecyclePolicyTimeUnit: TypeAlias = Literal[
    "DAYS",
    "WEEKS",
    "MONTHS",
    "YEARS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DAYS",
        "WEEKS",
        "MONTHS",
        "YEARS",
    )
)


def serialize_json(value: LifecyclePolicyTimeUnit) -> str:
    return value


def deserialize_json(data: str) -> LifecyclePolicyTimeUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LifecyclePolicyTimeUnit value: {data!r}")
    return cast(LifecyclePolicyTimeUnit, data)
