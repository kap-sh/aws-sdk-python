"""Generated from Smithy shape ``com.amazonaws.bedrock#EntitlementAvailability``."""

from typing import Literal, TypeAlias, cast

EntitlementAvailability: TypeAlias = Literal[
    "AVAILABLE",
    "NOT_AVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EntitlementAvailability) -> str:
    return value


def deserialize_json(data: str) -> EntitlementAvailability:
    return cast(EntitlementAvailability, data)
