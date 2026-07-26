"""Generated from Smithy shape ``com.amazonaws.outposts#FiberOpticCableType``."""

from typing import Literal, TypeAlias, cast

FiberOpticCableType: TypeAlias = Literal[
    "SINGLE_MODE",
    "MULTI_MODE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FiberOpticCableType) -> str:
    return value


def deserialize_json(data: str) -> FiberOpticCableType:
    return cast(FiberOpticCableType, data)
