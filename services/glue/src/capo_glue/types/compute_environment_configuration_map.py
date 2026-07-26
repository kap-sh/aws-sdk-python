"""Generated from Smithy shape ``com.amazonaws.glue#ComputeEnvironmentConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.compute_environment_configuration
    import capo_glue.types.compute_environment_name

ComputeEnvironmentConfigurationMap: TypeAlias = dict[
    "capo_glue.types.compute_environment_name.ComputeEnvironmentName",
    "capo_glue.types.compute_environment_configuration.ComputeEnvironmentConfiguration",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: ComputeEnvironmentConfigurationMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.compute_environment_configuration

        out[key] = (
            capo_glue.types.compute_environment_configuration.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeEnvironmentConfigurationMap:
    out: ComputeEnvironmentConfigurationMap = {}
    for key, value in data.items():
        import capo_glue.types.compute_environment_configuration

        out[key] = (
            capo_glue.types.compute_environment_configuration.deserialize_aws_json_1_1(
                value
            )
        )
    return out
