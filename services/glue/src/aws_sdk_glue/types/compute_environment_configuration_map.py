"""Generated from Smithy shape ``com.amazonaws.glue#ComputeEnvironmentConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.compute_environment_configuration
    import aws_sdk_glue.types.compute_environment_name

ComputeEnvironmentConfigurationMap: TypeAlias = dict[
    "aws_sdk_glue.types.compute_environment_name.ComputeEnvironmentName",
    "aws_sdk_glue.types.compute_environment_configuration.ComputeEnvironmentConfiguration",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: ComputeEnvironmentConfigurationMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_glue.types.compute_environment_configuration

        out[key] = (
            aws_sdk_glue.types.compute_environment_configuration.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ComputeEnvironmentConfigurationMap:
    out: ComputeEnvironmentConfigurationMap = {}
    for key, value in data.items():
        import aws_sdk_glue.types.compute_environment_configuration

        out[key] = (
            aws_sdk_glue.types.compute_environment_configuration.deserialize_aws_json_1_1(
                value
            )
        )
    return out
