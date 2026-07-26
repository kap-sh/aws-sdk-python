"""Generated from Smithy shape ``com.amazonaws.opensearch#InitiatedBy``."""

from typing import Literal, TypeAlias, cast

InitiatedBy: TypeAlias = Literal[
    "CUSTOMER",
    "SERVICE",
]


# --- restJson1 ser/de ---
def serialize_json(value: InitiatedBy) -> str:
    return value


def deserialize_json(data: str) -> InitiatedBy:
    return cast(InitiatedBy, data)
