"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTagMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.map_key
    import aws_sdk_inspector2.types.map_value

CisTagMap: TypeAlias = dict[
    "aws_sdk_inspector2.types.map_key.MapKey",
    "aws_sdk_inspector2.types.map_value.MapValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CisTagMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> CisTagMap:
    out: CisTagMap = {}
    for key, value in data.items():
        out[key] = value
    return out
