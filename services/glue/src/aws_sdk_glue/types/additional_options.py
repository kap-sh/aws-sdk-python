"""Generated from Smithy shape ``com.amazonaws.glue#AdditionalOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property

AdditionalOptions: TypeAlias = dict[
    "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty",
    "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AdditionalOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> AdditionalOptions:
    out: AdditionalOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
