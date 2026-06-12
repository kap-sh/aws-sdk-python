"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PhysicalIdentifierType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

PhysicalIdentifierType: TypeAlias = Literal[
    "Arn",
    "Native",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Arn",
        "Native",
    )
)


def serialize_json(value: PhysicalIdentifierType) -> str:
    return value


def deserialize_json(data: str) -> PhysicalIdentifierType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhysicalIdentifierType value: {data!r}")
    return cast(PhysicalIdentifierType, data)
