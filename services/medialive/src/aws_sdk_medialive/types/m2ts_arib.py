"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsArib``."""

from typing import Literal, TypeAlias, cast

"""M2ts Arib"""
M2tsArib: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsArib) -> str:
    return value


def deserialize_json(data: str) -> M2tsArib:
    return cast(M2tsArib, data)
