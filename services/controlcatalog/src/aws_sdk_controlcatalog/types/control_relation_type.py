"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlRelationType``."""

from typing import Literal, TypeAlias, cast

ControlRelationType: TypeAlias = Literal[
    "COMPLEMENTARY",
    "ALTERNATIVE",
    "MUTUALLY_EXCLUSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlRelationType) -> str:
    return value


def deserialize_json(data: str) -> ControlRelationType:
    return cast(ControlRelationType, data)
