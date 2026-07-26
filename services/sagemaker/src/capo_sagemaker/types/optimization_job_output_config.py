"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.optimization_sage_maker_model
    import capo_sagemaker.types.s3_uri


class OptimizationJobOutputConfig(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of a key in Amazon Web Services KMS. SageMaker uses they key to encrypt the artifacts of the optimized model when SageMaker uploads the model to Amazon S3.</p>"""
    s3_output_location: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 URI for where to store the optimized model that you create with an optimization job.</p>"""
    sage_maker_model: NotRequired[
        "capo_sagemaker.types.optimization_sage_maker_model.OptimizationSageMakerModel"
    ]
    """<p>The name of a SageMaker model to use as the output destination for an optimization job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationJobOutputConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "s3_output_location" in value:
        out["S3OutputLocation"] = value["s3_output_location"]
    if "sage_maker_model" in value:
        import capo_sagemaker.types.optimization_sage_maker_model

        out["SageMakerModel"] = (
            capo_sagemaker.types.optimization_sage_maker_model.serialize_aws_json_1_1(
                value["sage_maker_model"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationJobOutputConfig:
    out: OptimizationJobOutputConfig = {}  # type: ignore[typeddict-item]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "S3OutputLocation" in data:
        out["s3_output_location"] = data["S3OutputLocation"]
    if "SageMakerModel" in data:
        import capo_sagemaker.types.optimization_sage_maker_model

        out["sage_maker_model"] = (
            capo_sagemaker.types.optimization_sage_maker_model.deserialize_aws_json_1_1(
                data["SageMakerModel"]
            )
        )
    return out
