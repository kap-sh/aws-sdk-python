"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemRelationship``."""

from typing import Literal, TypeAlias, cast

CustomLineItemRelationship: TypeAlias = Literal[
    "PARENT",
    "CHILD",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemRelationship) -> str:
    return value


def deserialize_json(data: str) -> CustomLineItemRelationship:
    return cast(CustomLineItemRelationship, data)
