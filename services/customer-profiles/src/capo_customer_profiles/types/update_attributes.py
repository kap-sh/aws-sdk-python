"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.string0_to255
    import capo_customer_profiles.types.string1_to255

UpdateAttributes: TypeAlias = dict[
    "capo_customer_profiles.types.string1_to255.string1To255",
    "capo_customer_profiles.types.string0_to255.string0To255",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UpdateAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> UpdateAttributes:
    out: UpdateAttributes = {}
    for key, value in data.items():
        out[key] = value
    return out
