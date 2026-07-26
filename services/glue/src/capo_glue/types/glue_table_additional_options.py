"""Generated from Smithy shape ``com.amazonaws.glue#GlueTableAdditionalOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.name_string

GlueTableAdditionalOptions: TypeAlias = dict[
    "capo_glue.types.name_string.NameString",
    "capo_glue.types.description_string.DescriptionString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: GlueTableAdditionalOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> GlueTableAdditionalOptions:
    out: GlueTableAdditionalOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
