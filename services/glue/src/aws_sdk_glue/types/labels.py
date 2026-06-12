"""Generated from Smithy shape ``com.amazonaws.glue#Labels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string

Labels: TypeAlias = dict[
    "aws_sdk_glue.types.name_string.NameString",
    "aws_sdk_glue.types.name_string.NameString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Labels) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Labels:
    out: Labels = {}
    for key, value in data.items():
        out[key] = value
    return out
