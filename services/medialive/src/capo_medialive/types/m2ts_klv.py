"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsKlv``."""

from typing import Literal, TypeAlias, cast

"""M2ts Klv"""
M2tsKlv: TypeAlias = Literal[
    "NONE",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsKlv) -> str:
    return value


def deserialize_json(data: str) -> M2tsKlv:
    return cast(M2tsKlv, data)
