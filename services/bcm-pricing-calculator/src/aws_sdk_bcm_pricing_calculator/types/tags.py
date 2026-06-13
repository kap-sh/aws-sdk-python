"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.resource_tag_key
    import aws_sdk_bcm_pricing_calculator.types.resource_tag_value

Tags: TypeAlias = dict[
    "aws_sdk_bcm_pricing_calculator.types.resource_tag_key.ResourceTagKey",
    "aws_sdk_bcm_pricing_calculator.types.resource_tag_value.ResourceTagValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: Tags) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> Tags:
    out: Tags = {}
    for key, value in data.items():
        out[key] = value
    return out
