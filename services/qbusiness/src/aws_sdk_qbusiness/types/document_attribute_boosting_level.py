"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeBoostingLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

DocumentAttributeBoostingLevel: TypeAlias = Literal[
    "NONE",
    "LOW",
    "MEDIUM",
    "HIGH",
    "VERY_HIGH",
    "ONE",
    "TWO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
        "ONE",
        "TWO",
    )
)


def serialize_json(value: DocumentAttributeBoostingLevel) -> str:
    return value


def deserialize_json(data: str) -> DocumentAttributeBoostingLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DocumentAttributeBoostingLevel value: {data!r}"
        )
    return cast(DocumentAttributeBoostingLevel, data)
