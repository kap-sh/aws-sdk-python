"""Generated from Smithy shape ``com.amazonaws.outposts#RackUnitHeight``."""

from typing import Literal, TypeAlias, cast

RackUnitHeight: TypeAlias = Literal[
    "HEIGHT_42U",
    "HEIGHT_2U",
    "HEIGHT_1U",
]


# --- restJson1 ser/de ---
def serialize_json(value: RackUnitHeight) -> str:
    return value


def deserialize_json(data: str) -> RackUnitHeight:
    return cast(RackUnitHeight, data)
