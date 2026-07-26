"""Generated from Smithy shape ``com.amazonaws.datazone#GlossaryTermStatus``."""

from typing import Literal, TypeAlias, cast

GlossaryTermStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GlossaryTermStatus) -> str:
    return value


def deserialize_json(data: str) -> GlossaryTermStatus:
    return cast(GlossaryTermStatus, data)
