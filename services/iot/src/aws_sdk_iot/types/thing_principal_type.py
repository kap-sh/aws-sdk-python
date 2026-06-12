"""Generated from Smithy shape ``com.amazonaws.iot#ThingPrincipalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ThingPrincipalType: TypeAlias = Literal[
    "EXCLUSIVE_THING",
    "NON_EXCLUSIVE_THING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXCLUSIVE_THING",
        "NON_EXCLUSIVE_THING",
    )
)


def serialize_json(value: ThingPrincipalType) -> str:
    return value


def deserialize_json(data: str) -> ThingPrincipalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThingPrincipalType value: {data!r}")
    return cast(ThingPrincipalType, data)
