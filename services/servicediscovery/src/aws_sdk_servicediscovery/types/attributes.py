"""Generated from Smithy shape ``com.amazonaws.servicediscovery#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.attr_key
    import aws_sdk_servicediscovery.types.attr_value

Attributes: TypeAlias = dict[
    "aws_sdk_servicediscovery.types.attr_key.AttrKey",
    "aws_sdk_servicediscovery.types.attr_value.AttrValue",
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
