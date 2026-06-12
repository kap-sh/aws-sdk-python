"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemRelationship``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billingconductor.errors import DeserializationError

CustomLineItemRelationship: TypeAlias = Literal[
    "PARENT",
    "CHILD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PARENT",
        "CHILD",
    )
)


def serialize_json(value: CustomLineItemRelationship) -> str:
    return value


def deserialize_json(data: str) -> CustomLineItemRelationship:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomLineItemRelationship value: {data!r}"
        )
    return cast(CustomLineItemRelationship, data)
