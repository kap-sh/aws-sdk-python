"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentContainerSpecificationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.deployed_image
    import capo_sagemaker.types.environment_map
    import capo_sagemaker.types.url


class InferenceComponentContainerSpecificationSummary(TypedDict, closed=True):
    deployed_image: NotRequired["capo_sagemaker.types.deployed_image.DeployedImage"]
    artifact_url: NotRequired["capo_sagemaker.types.url.Url"]
    """<p>The Amazon S3 path where the model artifacts are stored.</p>"""
    environment: NotRequired["capo_sagemaker.types.environment_map.EnvironmentMap"]
    """<p>The environment variables to set in the Docker container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: InferenceComponentContainerSpecificationSummary,
) -> dict:
    out: dict = {}
    if "deployed_image" in value:
        import capo_sagemaker.types.deployed_image

        out["DeployedImage"] = (
            capo_sagemaker.types.deployed_image.serialize_aws_json_1_1(
                value["deployed_image"]
            )
        )
    if "artifact_url" in value:
        out["ArtifactUrl"] = value["artifact_url"]
    if "environment" in value:
        import capo_sagemaker.types.environment_map

        out["Environment"] = (
            capo_sagemaker.types.environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> InferenceComponentContainerSpecificationSummary:
    out: InferenceComponentContainerSpecificationSummary = {}  # type: ignore[typeddict-item]
    if "DeployedImage" in data:
        import capo_sagemaker.types.deployed_image

        out["deployed_image"] = (
            capo_sagemaker.types.deployed_image.deserialize_aws_json_1_1(
                data["DeployedImage"]
            )
        )
    if "ArtifactUrl" in data:
        out["artifact_url"] = data["ArtifactUrl"]
    if "Environment" in data:
        import capo_sagemaker.types.environment_map

        out["environment"] = (
            capo_sagemaker.types.environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    return out
