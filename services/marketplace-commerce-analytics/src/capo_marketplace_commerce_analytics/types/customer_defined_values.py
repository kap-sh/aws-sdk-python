"""Generated from Smithy shape ``com.amazonaws.marketplacecommerceanalytics#CustomerDefinedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_commerce_analytics.types.optional_key
    import capo_marketplace_commerce_analytics.types.optional_value

CustomerDefinedValues: TypeAlias = dict[
    "capo_marketplace_commerce_analytics.types.optional_key.OptionalKey",
    "capo_marketplace_commerce_analytics.types.optional_value.OptionalValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CustomerDefinedValues) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerDefinedValues:
    out: CustomerDefinedValues = {}
    for key, value in data.items():
        out[key] = value
    return out
