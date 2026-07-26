"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobModelSourceS3``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.optimization_model_access_config
    import capo_sagemaker.types.s3_uri


class OptimizationJobModelSourceS3(TypedDict, closed=True):
    s3_uri: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>An Amazon S3 URI that locates a source model to optimize with an optimization job.</p>"""
    model_access_config: NotRequired[
        "capo_sagemaker.types.optimization_model_access_config.OptimizationModelAccessConfig"
    ]
    """<p>The access configuration settings for the source ML model for an optimization job, where you can accept the model end-user license agreement (EULA).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationJobModelSourceS3) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    if "model_access_config" in value:
        import capo_sagemaker.types.optimization_model_access_config

        out["ModelAccessConfig"] = (
            capo_sagemaker.types.optimization_model_access_config.serialize_aws_json_1_1(
                value["model_access_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationJobModelSourceS3:
    out: OptimizationJobModelSourceS3 = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    if "ModelAccessConfig" in data:
        import capo_sagemaker.types.optimization_model_access_config

        out["model_access_config"] = (
            capo_sagemaker.types.optimization_model_access_config.deserialize_aws_json_1_1(
                data["ModelAccessConfig"]
            )
        )
    return out
