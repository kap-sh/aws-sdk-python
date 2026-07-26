"""Generated from Smithy shape ``com.amazonaws.tnb#OperationalState``."""

from typing import Literal, TypeAlias, cast

OperationalState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationalState) -> str:
    return value


def deserialize_json(data: str) -> OperationalState:
    return cast(OperationalState, data)
