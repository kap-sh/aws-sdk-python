"""Generated from Smithy shape ``com.amazonaws.sagemaker#AuthenticationRequestExtraParams``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.authentication_request_extra_params_key
    import capo_sagemaker.types.authentication_request_extra_params_value

AuthenticationRequestExtraParams: TypeAlias = dict[
    "capo_sagemaker.types.authentication_request_extra_params_key.AuthenticationRequestExtraParamsKey",
    "capo_sagemaker.types.authentication_request_extra_params_value.AuthenticationRequestExtraParamsValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: AuthenticationRequestExtraParams,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationRequestExtraParams:
    out: AuthenticationRequestExtraParams = {}
    for key, value in data.items():
        out[key] = value
    return out
