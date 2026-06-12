"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#Context``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.attribute_name
    import aws_sdk_personalize_runtime.types.attribute_value

Context: TypeAlias = dict[
    "aws_sdk_personalize_runtime.types.attribute_name.AttributeName",
    "aws_sdk_personalize_runtime.types.attribute_value.AttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: Context) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> Context:
    out: Context = {}
    for key, value in data.items():
        out[key] = value
    return out
