"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

IdMappingType: TypeAlias = Literal[
    "PROVIDER",
    "RULE_BASED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROVIDER",
        "RULE_BASED",
    )
)


def serialize_json(value: IdMappingType) -> str:
    return value


def deserialize_json(data: str) -> IdMappingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdMappingType value: {data!r}")
    return cast(IdMappingType, data)
