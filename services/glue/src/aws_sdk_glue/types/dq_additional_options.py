"""Generated from Smithy shape ``com.amazonaws.glue#DQAdditionalOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.additional_option_keys
    import aws_sdk_glue.types.generic_string

DQAdditionalOptions: TypeAlias = dict[
    "aws_sdk_glue.types.additional_option_keys.AdditionalOptionKeys",
    "aws_sdk_glue.types.generic_string.GenericString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DQAdditionalOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_glue.types.additional_option_keys

        out[aws_sdk_glue.types.additional_option_keys.serialize_aws_json_1_1(key)] = (
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DQAdditionalOptions:
    out: DQAdditionalOptions = {}
    for key, value in data.items():
        import aws_sdk_glue.types.additional_option_keys

        out[aws_sdk_glue.types.additional_option_keys.deserialize_aws_json_1_1(key)] = (
            value
        )
    return out
