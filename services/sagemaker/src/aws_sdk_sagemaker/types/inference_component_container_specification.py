"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentContainerSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.container_image
    import aws_sdk_sagemaker.types.environment_map
    import aws_sdk_sagemaker.types.url


class InferenceComponentContainerSpecification(TypedDict):
    image: NotRequired["aws_sdk_sagemaker.types.container_image.ContainerImage"]
    """<p>The Amazon Elastic Container Registry (Amazon ECR) path where the Docker image for the model is stored.</p>"""
    artifact_url: NotRequired["aws_sdk_sagemaker.types.url.Url"]
    """<p>The Amazon S3 path where the model artifacts, which result from model training, are stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).</p>"""
    environment: NotRequired["aws_sdk_sagemaker.types.environment_map.EnvironmentMap"]
    """<p>The environment variables to set in the Docker container. Each key and value in the Environment string-to-string map can have length of up to 1024. We support up to 16 entries in the map.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentContainerSpecification) -> dict:
    out: dict = {}
    if "image" in value:
        out["Image"] = value["image"]
    if "artifact_url" in value:
        out["ArtifactUrl"] = value["artifact_url"]
    if "environment" in value:
        import aws_sdk_sagemaker.types.environment_map

        out["Environment"] = (
            aws_sdk_sagemaker.types.environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentContainerSpecification:
    out: InferenceComponentContainerSpecification = {}  # type: ignore[typeddict-item]
    if "Image" in data:
        out["image"] = data["Image"]
    if "ArtifactUrl" in data:
        out["artifact_url"] = data["ArtifactUrl"]
    if "Environment" in data:
        import aws_sdk_sagemaker.types.environment_map

        out["environment"] = (
            aws_sdk_sagemaker.types.environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    return out
