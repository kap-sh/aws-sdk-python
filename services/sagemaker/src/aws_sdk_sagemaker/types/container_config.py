"""Generated from Smithy shape ``com.amazonaws.sagemaker#ContainerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.custom_image_container_arguments
    import aws_sdk_sagemaker.types.custom_image_container_entrypoint
    import aws_sdk_sagemaker.types.custom_image_container_environment_variables


class ContainerConfig(TypedDict, closed=True):
    container_arguments: NotRequired[
        "aws_sdk_sagemaker.types.custom_image_container_arguments.CustomImageContainerArguments"
    ]
    """<p>The arguments for the container when you're running the application.</p>"""
    container_entrypoint: NotRequired[
        "aws_sdk_sagemaker.types.custom_image_container_entrypoint.CustomImageContainerEntrypoint"
    ]
    """<p>The entrypoint used to run the application in the container.</p>"""
    container_environment_variables: NotRequired[
        "aws_sdk_sagemaker.types.custom_image_container_environment_variables.CustomImageContainerEnvironmentVariables"
    ]
    """<p>The environment variables to set in the container</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerConfig) -> dict:
    out: dict = {}
    if "container_arguments" in value:
        import aws_sdk_sagemaker.types.custom_image_container_arguments

        out["ContainerArguments"] = (
            aws_sdk_sagemaker.types.custom_image_container_arguments.serialize_aws_json_1_1(
                value["container_arguments"]
            )
        )
    if "container_entrypoint" in value:
        import aws_sdk_sagemaker.types.custom_image_container_entrypoint

        out["ContainerEntrypoint"] = (
            aws_sdk_sagemaker.types.custom_image_container_entrypoint.serialize_aws_json_1_1(
                value["container_entrypoint"]
            )
        )
    if "container_environment_variables" in value:
        import aws_sdk_sagemaker.types.custom_image_container_environment_variables

        out["ContainerEnvironmentVariables"] = (
            aws_sdk_sagemaker.types.custom_image_container_environment_variables.serialize_aws_json_1_1(
                value["container_environment_variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerConfig:
    out: ContainerConfig = {}  # type: ignore[typeddict-item]
    if "ContainerArguments" in data:
        import aws_sdk_sagemaker.types.custom_image_container_arguments

        out["container_arguments"] = (
            aws_sdk_sagemaker.types.custom_image_container_arguments.deserialize_aws_json_1_1(
                data["ContainerArguments"]
            )
        )
    if "ContainerEntrypoint" in data:
        import aws_sdk_sagemaker.types.custom_image_container_entrypoint

        out["container_entrypoint"] = (
            aws_sdk_sagemaker.types.custom_image_container_entrypoint.deserialize_aws_json_1_1(
                data["ContainerEntrypoint"]
            )
        )
    if "ContainerEnvironmentVariables" in data:
        import aws_sdk_sagemaker.types.custom_image_container_environment_variables

        out["container_environment_variables"] = (
            aws_sdk_sagemaker.types.custom_image_container_environment_variables.deserialize_aws_json_1_1(
                data["ContainerEnvironmentVariables"]
            )
        )
    return out
