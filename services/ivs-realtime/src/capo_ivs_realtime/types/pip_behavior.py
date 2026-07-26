"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#PipBehavior``."""

from typing import Literal, TypeAlias, cast

PipBehavior: TypeAlias = Literal[
    "STATIC",
    "DYNAMIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: PipBehavior) -> str:
    return value


def deserialize_json(data: str) -> PipBehavior:
    return cast(PipBehavior, data)
