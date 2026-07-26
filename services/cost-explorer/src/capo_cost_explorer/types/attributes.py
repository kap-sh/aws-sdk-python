"""Generated from Smithy shape ``com.amazonaws.costexplorer#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_explorer.types.attribute_type
    import capo_cost_explorer.types.attribute_value

Attributes: TypeAlias = dict[
    "capo_cost_explorer.types.attribute_type.AttributeType",
    "capo_cost_explorer.types.attribute_value.AttributeValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Attributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Attributes:
    out: Attributes = {}
    for key, value in data.items():
        out[key] = value
    return out
