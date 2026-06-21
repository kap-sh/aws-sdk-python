"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlScope``."""

from typing import Literal, TypeAlias, cast

ControlScope: TypeAlias = Literal[
    "GLOBAL",
    "REGIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlScope) -> str:
    return value


def deserialize_json(data: str) -> ControlScope:
    return cast(ControlScope, data)
