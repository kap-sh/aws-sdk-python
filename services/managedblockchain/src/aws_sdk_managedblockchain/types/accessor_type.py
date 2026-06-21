"""Generated from Smithy shape ``com.amazonaws.managedblockchain#AccessorType``."""

from typing import Literal, TypeAlias, cast

AccessorType: TypeAlias = Literal["BILLING_TOKEN",]


# --- restJson1 ser/de ---
def serialize_json(value: AccessorType) -> str:
    return value


def deserialize_json(data: str) -> AccessorType:
    return cast(AccessorType, data)
