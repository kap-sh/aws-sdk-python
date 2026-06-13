"""Generated from Smithy shape ``com.amazonaws.qbusiness#NumberAttributeBoostingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

NumberAttributeBoostingType: TypeAlias = Literal[
    "PRIORITIZE_LARGER_VALUES",
    "PRIORITIZE_SMALLER_VALUES",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIORITIZE_LARGER_VALUES",
        "PRIORITIZE_SMALLER_VALUES",
    )
)


def serialize_json(value: NumberAttributeBoostingType) -> str:
    return value


def deserialize_json(data: str) -> NumberAttributeBoostingType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown NumberAttributeBoostingType value: {data!r}"
        )
    return cast(NumberAttributeBoostingType, data)
