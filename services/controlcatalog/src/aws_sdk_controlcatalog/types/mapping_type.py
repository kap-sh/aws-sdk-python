"""Generated from Smithy shape ``com.amazonaws.controlcatalog#MappingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controlcatalog.errors import DeserializationError

MappingType: TypeAlias = Literal[
    "FRAMEWORK",
    "COMMON_CONTROL",
    "RELATED_CONTROL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FRAMEWORK",
        "COMMON_CONTROL",
        "RELATED_CONTROL",
    )
)


def serialize_json(value: MappingType) -> str:
    return value


def deserialize_json(data: str) -> MappingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MappingType value: {data!r}")
    return cast(MappingType, data)
