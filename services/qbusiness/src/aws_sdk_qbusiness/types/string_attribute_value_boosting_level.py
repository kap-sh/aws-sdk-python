"""Generated from Smithy shape ``com.amazonaws.qbusiness#StringAttributeValueBoostingLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

StringAttributeValueBoostingLevel: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "VERY_HIGH",
    "ONE",
    "TWO",
    "THREE",
    "FOUR",
    "FIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
        "VERY_HIGH",
        "ONE",
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
    )
)


def serialize_json(value: StringAttributeValueBoostingLevel) -> str:
    return value


def deserialize_json(data: str) -> StringAttributeValueBoostingLevel:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StringAttributeValueBoostingLevel value: {data!r}"
        )
    return cast(StringAttributeValueBoostingLevel, data)
