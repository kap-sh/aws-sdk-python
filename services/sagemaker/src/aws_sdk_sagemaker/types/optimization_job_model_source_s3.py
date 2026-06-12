"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobModelSourceS3``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.optimization_model_access_config
    import aws_sdk_sagemaker.types.s3_uri


class OptimizationJobModelSourceS3(TypedDict):
    s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>An Amazon S3 URI that locates a source model to optimize with an optimization job.</p>"""
    model_access_config: NotRequired[
        "aws_sdk_sagemaker.types.optimization_model_access_config.OptimizationModelAccessConfig"
    ]
    """<p>The access configuration settings for the source ML model for an optimization job, where you can accept the model end-user license agreement (EULA).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationJobModelSourceS3) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "model_access_config" in value:
        import aws_sdk_sagemaker.types.optimization_model_access_config

        out["ModelAccessConfig"] = (
            aws_sdk_sagemaker.types.optimization_model_access_config.serialize_aws_json_1_1(
                value["model_access_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationJobModelSourceS3:
    out: OptimizationJobModelSourceS3 = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    if "ModelAccessConfig" in data:
        import aws_sdk_sagemaker.types.optimization_model_access_config

        out["model_access_config"] = (
            aws_sdk_sagemaker.types.optimization_model_access_config.deserialize_aws_json_1_1(
                data["ModelAccessConfig"]
            )
        )
    return out
