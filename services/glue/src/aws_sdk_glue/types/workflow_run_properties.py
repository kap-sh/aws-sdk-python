"""Generated from Smithy shape ``com.amazonaws.glue#WorkflowRunProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.id_string

WorkflowRunProperties: TypeAlias = dict[
    "aws_sdk_glue.types.id_string.IdString",
    "aws_sdk_glue.types.generic_string.GenericString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: WorkflowRunProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkflowRunProperties:
    out: WorkflowRunProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
