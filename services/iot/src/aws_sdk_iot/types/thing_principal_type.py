"""Generated from Smithy shape ``com.amazonaws.iot#ThingPrincipalType``."""

from typing import Literal, TypeAlias, cast

ThingPrincipalType: TypeAlias = Literal[
    "EXCLUSIVE_THING",
    "NON_EXCLUSIVE_THING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ThingPrincipalType) -> str:
    return value


def deserialize_json(data: str) -> ThingPrincipalType:
    return cast(ThingPrincipalType, data)
