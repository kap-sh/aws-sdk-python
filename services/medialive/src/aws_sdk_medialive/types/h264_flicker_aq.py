"""Generated from Smithy shape ``com.amazonaws.medialive#H264FlickerAq``."""

from typing import Literal, TypeAlias, cast

"""H264 Flicker Aq"""
H264FlickerAq: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264FlickerAq) -> str:
    return value


def deserialize_json(data: str) -> H264FlickerAq:
    return cast(H264FlickerAq, data)
