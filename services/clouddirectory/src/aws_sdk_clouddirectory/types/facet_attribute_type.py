"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

FacetAttributeType: TypeAlias = Literal[
    "STRING",
    "BINARY",
    "BOOLEAN",
    "NUMBER",
    "DATETIME",
    "VARIANT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "BINARY",
        "BOOLEAN",
        "NUMBER",
        "DATETIME",
        "VARIANT",
    )
)


def serialize_json(value: FacetAttributeType) -> str:
    return value


def deserialize_json(data: str) -> FacetAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FacetAttributeType value: {data!r}")
    return cast(FacetAttributeType, data)
