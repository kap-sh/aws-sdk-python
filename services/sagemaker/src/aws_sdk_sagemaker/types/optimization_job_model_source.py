"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobModelSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.optimization_job_model_source_s3
    import aws_sdk_sagemaker.types.optimization_sage_maker_model


class OptimizationJobModelSource(TypedDict):
    s3: NotRequired[
        "aws_sdk_sagemaker.types.optimization_job_model_source_s3.OptimizationJobModelSourceS3"
    ]
    """<p>The Amazon S3 location of a source model to optimize with an optimization job.</p>"""
    sage_maker_model: NotRequired[
        "aws_sdk_sagemaker.types.optimization_sage_maker_model.OptimizationSageMakerModel"
    ]
    """<p>The name of an existing SageMaker model to optimize with an optimization job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationJobModelSource) -> dict:
    out: dict = {}
    if "s3" in value:
        import aws_sdk_sagemaker.types.optimization_job_model_source_s3

        out["S3"] = (
            aws_sdk_sagemaker.types.optimization_job_model_source_s3.serialize_aws_json_1_1(
                value["s3"]
            )
        )
    if "sage_maker_model" in value:
        import aws_sdk_sagemaker.types.optimization_sage_maker_model

        out["SageMakerModel"] = (
            aws_sdk_sagemaker.types.optimization_sage_maker_model.serialize_aws_json_1_1(
                value["sage_maker_model"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationJobModelSource:
    out: OptimizationJobModelSource = {}  # type: ignore[typeddict-item]
    if "S3" in data:
        import aws_sdk_sagemaker.types.optimization_job_model_source_s3

        out["s3"] = (
            aws_sdk_sagemaker.types.optimization_job_model_source_s3.deserialize_aws_json_1_1(
                data["S3"]
            )
        )
    if "SageMakerModel" in data:
        import aws_sdk_sagemaker.types.optimization_sage_maker_model

        out["sage_maker_model"] = (
            aws_sdk_sagemaker.types.optimization_sage_maker_model.deserialize_aws_json_1_1(
                data["SageMakerModel"]
            )
        )
    return out
