"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#DukptKeyVariant``."""

from typing import Literal, TypeAlias, cast

DukptKeyVariant: TypeAlias = Literal[
    "BIDIRECTIONAL",
    "REQUEST",
    "RESPONSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DukptKeyVariant) -> str:
    return value


def deserialize_json(data: str) -> DukptKeyVariant:
    return cast(DukptKeyVariant, data)
