"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CustomAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_dimension
    import capo_customer_profiles.types.string1_to255

CustomAttributes: TypeAlias = dict[
    "capo_customer_profiles.types.string1_to255.string1To255",
    "capo_customer_profiles.types.attribute_dimension.AttributeDimension",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CustomAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_customer_profiles.types.attribute_dimension

        out[key] = capo_customer_profiles.types.attribute_dimension.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> CustomAttributes:
    out: CustomAttributes = {}
    for key, value in data.items():
        import capo_customer_profiles.types.attribute_dimension

        out[key] = capo_customer_profiles.types.attribute_dimension.deserialize_json(
            value
        )
    return out
