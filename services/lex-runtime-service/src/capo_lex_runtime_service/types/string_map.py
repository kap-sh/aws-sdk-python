"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#StringMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_service.types.string

StringMap: TypeAlias = dict[
    "capo_lex_runtime_service.types.string.String",
    "capo_lex_runtime_service.types.string.String",
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
