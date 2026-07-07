"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmValidationProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.training_job_definition
    import aws_sdk_sagemaker.types.transform_job_definition


class AlgorithmValidationProfile(TypedDict, closed=True):
    profile_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>The name of the profile for the algorithm. The name must have 1 to 63 characters. Valid characters are a-z, A-Z, 0-9, and - (hyphen).</p>"""
    training_job_definition: NotRequired[
        "aws_sdk_sagemaker.types.training_job_definition.TrainingJobDefinition"
    ]
    """<p>The <code>TrainingJobDefinition</code> object that describes the training job that SageMaker runs to validate your algorithm.</p>"""
    transform_job_definition: NotRequired[
        "aws_sdk_sagemaker.types.transform_job_definition.TransformJobDefinition"
    ]
    """<p>The <code>TransformJobDefinition</code> object that describes the transform job that SageMaker runs to validate your algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmValidationProfile) -> dict:
    out: dict = {}
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "training_job_definition" in value:
        import aws_sdk_sagemaker.types.training_job_definition

        out["TrainingJobDefinition"] = (
            aws_sdk_sagemaker.types.training_job_definition.serialize_aws_json_1_1(
                value["training_job_definition"]
            )
        )
    if "transform_job_definition" in value:
        import aws_sdk_sagemaker.types.transform_job_definition

        out["TransformJobDefinition"] = (
            aws_sdk_sagemaker.types.transform_job_definition.serialize_aws_json_1_1(
                value["transform_job_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlgorithmValidationProfile:
    out: AlgorithmValidationProfile = {}  # type: ignore[typeddict-item]
    if "ProfileName" in data:
        out["profile_name"] = data["ProfileName"]
    if "TrainingJobDefinition" in data:
        import aws_sdk_sagemaker.types.training_job_definition

        out["training_job_definition"] = (
            aws_sdk_sagemaker.types.training_job_definition.deserialize_aws_json_1_1(
                data["TrainingJobDefinition"]
            )
        )
    if "TransformJobDefinition" in data:
        import aws_sdk_sagemaker.types.transform_job_definition

        out["transform_job_definition"] = (
            aws_sdk_sagemaker.types.transform_job_definition.deserialize_aws_json_1_1(
                data["TransformJobDefinition"]
            )
        )
    return out
