"""Generated from Smithy shape ``com.amazonaws.apprunner#RuntimeEnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.runtime_environment_variables_key
    import aws_sdk_apprunner.types.runtime_environment_variables_value

RuntimeEnvironmentVariables: TypeAlias = dict[
    "aws_sdk_apprunner.types.runtime_environment_variables_key.RuntimeEnvironmentVariablesKey",
    "aws_sdk_apprunner.types.runtime_environment_variables_value.RuntimeEnvironmentVariablesValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RuntimeEnvironmentVariables) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> RuntimeEnvironmentVariables:
    out: RuntimeEnvironmentVariables = {}
    for key, value in data.items():
        out[key] = value
    return out
