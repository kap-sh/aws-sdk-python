"""Generated from Smithy shape ``com.amazonaws.connect#UserTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.string

UserTagMap: TypeAlias = dict[
    "capo_connect.types.string.String", "capo_connect.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UserTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> UserTagMap:
    out: UserTagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
