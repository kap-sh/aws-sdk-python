"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#StringMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.non_empty_string
    import capo_lex_runtime_v2.types.string

StringMap: TypeAlias = dict[
    "capo_lex_runtime_v2.types.non_empty_string.NonEmptyString",
    "capo_lex_runtime_v2.types.string.String",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StringMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> StringMap:
    out: StringMap = {}
    for key, value in data.items():
        out[key] = value
    return out
