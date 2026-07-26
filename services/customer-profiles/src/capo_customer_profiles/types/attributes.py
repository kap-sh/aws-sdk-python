"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.string1_to255

Attributes: TypeAlias = dict[
    "capo_customer_profiles.types.string1_to255.string1To255",
    "capo_customer_profiles.types.string1_to255.string1To255",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Attributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Attributes:
    out: Attributes = {}
    for key, value in data.items():
        out[key] = value
    return out
