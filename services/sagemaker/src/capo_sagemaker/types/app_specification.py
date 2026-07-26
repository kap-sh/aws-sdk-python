"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.container_arguments
    import capo_sagemaker.types.container_entrypoint
    import capo_sagemaker.types.image_uri


class AppSpecification(TypedDict, closed=True):
    image_uri: NotRequired["capo_sagemaker.types.image_uri.ImageUri"]
    """<p>The container image to be run by the processing job.</p>"""
    container_entrypoint: NotRequired[
        "capo_sagemaker.types.container_entrypoint.ContainerEntrypoint"
    ]
    """<p>The entrypoint for a container used to run a processing job.</p>"""
    container_arguments: NotRequired[
        "capo_sagemaker.types.container_arguments.ContainerArguments"
    ]
    """<p>The arguments for a container used to run a processing job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppSpecification) -> dict:
    out: dict = {}
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "container_entrypoint" in value:
        import capo_sagemaker.types.container_entrypoint

        out["ContainerEntrypoint"] = (
            capo_sagemaker.types.container_entrypoint.serialize_aws_json_1_1(
                value["container_entrypoint"]
            )
        )
    if "container_arguments" in value:
        import capo_sagemaker.types.container_arguments

        out["ContainerArguments"] = (
            capo_sagemaker.types.container_arguments.serialize_aws_json_1_1(
                value["container_arguments"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AppSpecification:
    out: AppSpecification = {}  # type: ignore[typeddict-item]
    if "ImageUri" in data:
        out["image_uri"] = data["ImageUri"]
    if "ContainerEntrypoint" in data:
        import capo_sagemaker.types.container_entrypoint

        out["container_entrypoint"] = (
            capo_sagemaker.types.container_entrypoint.deserialize_aws_json_1_1(
                data["ContainerEntrypoint"]
            )
        )
    if "ContainerArguments" in data:
        import capo_sagemaker.types.container_arguments

        out["container_arguments"] = (
            capo_sagemaker.types.container_arguments.deserialize_aws_json_1_1(
                data["ContainerArguments"]
            )
        )
    return out
