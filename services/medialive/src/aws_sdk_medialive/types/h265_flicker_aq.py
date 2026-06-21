"""Generated from Smithy shape ``com.amazonaws.medialive#H265FlickerAq``."""

from typing import Literal, TypeAlias, cast

"""H265 Flicker Aq"""
H265FlickerAq: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265FlickerAq) -> str:
    return value


def deserialize_json(data: str) -> H265FlickerAq:
    return cast(H265FlickerAq, data)
