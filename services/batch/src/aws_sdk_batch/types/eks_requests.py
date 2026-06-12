"""Generated from Smithy shape ``com.amazonaws.batch#EksRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.quantity
    import aws_sdk_batch.types.string

EksRequests: TypeAlias = dict[
    "aws_sdk_batch.types.string.String", "aws_sdk_batch.types.quantity.Quantity"
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
