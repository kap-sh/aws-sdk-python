"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AttributeMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.attribute_name
    import capo_customer_profiles.types.filter_attribute_dimension

AttributeMap: TypeAlias = dict[
    "capo_customer_profiles.types.attribute_name.attributeName",
    "capo_customer_profiles.types.filter_attribute_dimension.FilterAttributeDimension",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AttributeMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_customer_profiles.types.filter_attribute_dimension

        out[key] = (
            capo_customer_profiles.types.filter_attribute_dimension.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> AttributeMap:
    out: AttributeMap = {}
    for key, value in data.items():
        import capo_customer_profiles.types.filter_attribute_dimension

        out[key] = (
            capo_customer_profiles.types.filter_attribute_dimension.deserialize_json(
                value
            )
        )
    return out
