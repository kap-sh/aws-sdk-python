"""Generated from Smithy shape ``com.amazonaws.apprunner#RuntimeEnvironmentSecrets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apprunner.types.runtime_environment_secrets_name
    import capo_apprunner.types.runtime_environment_secrets_value

RuntimeEnvironmentSecrets: TypeAlias = dict[
    "capo_apprunner.types.runtime_environment_secrets_name.RuntimeEnvironmentSecretsName",
    "capo_apprunner.types.runtime_environment_secrets_value.RuntimeEnvironmentSecretsValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: RuntimeEnvironmentSecrets) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> RuntimeEnvironmentSecrets:
    out: RuntimeEnvironmentSecrets = {}
    for key, value in data.items():
        out[key] = value
    return out
