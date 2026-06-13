"""Generated from Smithy shape ``com.amazonaws.entityresolution#ServiceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

ServiceType: TypeAlias = Literal[
    "ASSIGNMENT",
    "ID_MAPPING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASSIGNMENT",
        "ID_MAPPING",
    )
)


def serialize_json(value: ServiceType) -> str:
    return value


def deserialize_json(data: str) -> ServiceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceType value: {data!r}")
    return cast(ServiceType, data)
