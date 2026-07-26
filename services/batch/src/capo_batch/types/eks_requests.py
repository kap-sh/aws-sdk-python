"""Generated from Smithy shape ``com.amazonaws.batch#EksRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_batch.types.quantity
    import capo_batch.types.string

EksRequests: TypeAlias = dict[
    "capo_batch.types.string.String", "capo_batch.types.quantity.Quantity"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EksRequests) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EksRequests:
    out: EksRequests = {}
    for key, value in data.items():
        out[key] = value
    return out
