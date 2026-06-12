"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#FilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.filter_attribute_name
    import aws_sdk_personalize_runtime.types.filter_attribute_value

FilterValues: TypeAlias = dict[
    "aws_sdk_personalize_runtime.types.filter_attribute_name.FilterAttributeName",
    "aws_sdk_personalize_runtime.types.filter_attribute_value.FilterAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FilterValues) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FilterValues:
    out: FilterValues = {}
    for key, value in data.items():
        out[key] = value
    return out
