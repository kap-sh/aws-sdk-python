"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationOutputResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_mlflow_config
    import aws_sdk_sagemaker.types.ai_resource_identifier
    import aws_sdk_sagemaker.types.s3_uri


class AIRecommendationOutputResult(TypedDict):
    s3_output_location: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI where the recommendation job writes its output results.</p>"""
    model_package_group_identifier: NotRequired[
        "aws_sdk_sagemaker.types.ai_resource_identifier.AIResourceIdentifier"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the model package group where deployment-ready model packages are registered.</p>"""
    mlflow_config: NotRequired[
        "aws_sdk_sagemaker.types.ai_mlflow_config.AIMlflowConfig"
    ]
    """<p>The MLflow tracking configuration for the job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationOutputResult) -> dict:
    out: dict = {}
    if "s3_output_location" in value:
        out["S3OutputLocation"] = value["s3_output_location"]
    if "model_package_group_identifier" in value:
        out["ModelPackageGroupIdentifier"] = value["model_package_group_identifier"]
    if "mlflow_config" in value:
        import aws_sdk_sagemaker.types.ai_mlflow_config

        out["MlflowConfig"] = (
            aws_sdk_sagemaker.types.ai_mlflow_config.serialize_aws_json_1_1(
                value["mlflow_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationOutputResult:
    out: AIRecommendationOutputResult = {}  # type: ignore[typeddict-item]
    if "S3OutputLocation" in data:
        out["s3_output_location"] = data["S3OutputLocation"]
    if "ModelPackageGroupIdentifier" in data:
        out["model_package_group_identifier"] = data["ModelPackageGroupIdentifier"]
    if "MlflowConfig" in data:
        import aws_sdk_sagemaker.types.ai_mlflow_config

        out["mlflow_config"] = (
            aws_sdk_sagemaker.types.ai_mlflow_config.deserialize_aws_json_1_1(
                data["MlflowConfig"]
            )
        )
    return out
