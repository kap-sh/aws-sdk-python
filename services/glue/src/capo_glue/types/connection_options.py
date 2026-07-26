"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.option_key
    import capo_glue.types.option_value

ConnectionOptions: TypeAlias = dict[
    "capo_glue.types.option_key.OptionKey", "capo_glue.types.option_value.OptionValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ConnectionOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionOptions:
    out: ConnectionOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
