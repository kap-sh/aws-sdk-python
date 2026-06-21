"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlBehavior``."""

from typing import Literal, TypeAlias, cast

ControlBehavior: TypeAlias = Literal[
    "PREVENTIVE",
    "PROACTIVE",
    "DETECTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlBehavior) -> str:
    return value


def deserialize_json(data: str) -> ControlBehavior:
    return cast(ControlBehavior, data)
