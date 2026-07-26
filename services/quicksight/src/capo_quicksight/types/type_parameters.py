"""Generated from Smithy shape ``com.amazonaws.quicksight#TypeParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string

TypeParameters: TypeAlias = dict[
    "capo_quicksight.types.limited_string.LimitedString",
    "capo_quicksight.types.limited_string.LimitedString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: TypeParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> TypeParameters:
    out: TypeParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
