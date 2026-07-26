"""Generated from Smithy shape ``com.amazonaws.glue#TokenUrlParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.token_url_parameter_key
    import capo_glue.types.token_url_parameter_value

TokenUrlParametersMap: TypeAlias = dict[
    "capo_glue.types.token_url_parameter_key.TokenUrlParameterKey",
    "capo_glue.types.token_url_parameter_value.TokenUrlParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TokenUrlParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TokenUrlParametersMap:
    out: TokenUrlParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
