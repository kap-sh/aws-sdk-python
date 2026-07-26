"""Generated from Smithy shape ``com.amazonaws.batch#FirelensConfigurationOptionsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.string

FirelensConfigurationOptionsMap: TypeAlias = dict[
    "capo_batch.types.string.String", "capo_batch.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FirelensConfigurationOptionsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FirelensConfigurationOptionsMap:
    out: FirelensConfigurationOptionsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
