"""Generated from Smithy shape ``com.amazonaws.batch#EksAnnotationsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.string

EksAnnotationsMap: TypeAlias = dict[
    "capo_batch.types.string.String", "capo_batch.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EksAnnotationsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EksAnnotationsMap:
    out: EksAnnotationsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
