"""Generated from Smithy shape ``com.amazonaws.batch#EksLimits``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.quantity
    import capo_batch.types.string

EksLimits: TypeAlias = dict[
    "capo_batch.types.string.String", "capo_batch.types.quantity.Quantity"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EksLimits) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EksLimits:
    out: EksLimits = {}
    for key, value in data.items():
        out[key] = value
    return out
