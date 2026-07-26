"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.connection_property_key
    import capo_glue.types.value_string

ConnectionProperties: TypeAlias = dict[
    "capo_glue.types.connection_property_key.ConnectionPropertyKey",
    "capo_glue.types.value_string.ValueString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ConnectionProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.connection_property_key

        out[capo_glue.types.connection_property_key.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionProperties:
    out: ConnectionProperties = {}
    for key, value in data.items():
        import capo_glue.types.connection_property_key

        out[capo_glue.types.connection_property_key.deserialize_aws_json_1_1(key)] = (
            value
        )
    return out
