"""Generated from Smithy shape ``com.amazonaws.identitystore#Extensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.attribute_value
    import aws_sdk_identitystore.types.extension_name

Extensions: TypeAlias = dict[
    "aws_sdk_identitystore.types.extension_name.ExtensionName",
    "aws_sdk_identitystore.types.attribute_value.AttributeValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Extensions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Extensions:
    out: Extensions = {}
    for key, value in data.items():
        out[key] = value
    return out
