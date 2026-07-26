"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.generic_string

ConnectorOptions: TypeAlias = dict[
    "capo_glue.types.generic_string.GenericString",
    "capo_glue.types.generic_string.GenericString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ConnectorOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorOptions:
    out: ConnectorOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
