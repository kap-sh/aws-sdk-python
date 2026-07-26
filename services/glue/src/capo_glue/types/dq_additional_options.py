"""Generated from Smithy shape ``com.amazonaws.glue#DQAdditionalOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.additional_option_keys
    import capo_glue.types.generic_string

DQAdditionalOptions: TypeAlias = dict[
    "capo_glue.types.additional_option_keys.AdditionalOptionKeys",
    "capo_glue.types.generic_string.GenericString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: DQAdditionalOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.additional_option_keys

        out[capo_glue.types.additional_option_keys.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> DQAdditionalOptions:
    out: DQAdditionalOptions = {}
    for key, value in data.items():
        import capo_glue.types.additional_option_keys

        out[capo_glue.types.additional_option_keys.deserialize_aws_json_1_1(key)] = (
            value
        )
    return out
