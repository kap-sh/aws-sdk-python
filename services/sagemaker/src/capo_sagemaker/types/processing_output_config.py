"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.processing_outputs


class ProcessingOutputConfig(TypedDict, closed=True):
    outputs: NotRequired["capo_sagemaker.types.processing_outputs.ProcessingOutputs"]
    """<p>An array of outputs configuring the data to upload from the processing container.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt the processing job output. <code>KmsKeyId</code> can be an ID of a KMS key, ARN of a KMS key, or alias of a KMS key. The <code>KmsKeyId</code> is applied to all outputs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProcessingOutputConfig) -> dict:
    out: dict = {}
    if "outputs" in value:
        import capo_sagemaker.types.processing_outputs

        out["Outputs"] = capo_sagemaker.types.processing_outputs.serialize_aws_json_1_1(
            value["outputs"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingOutputConfig:
    out: ProcessingOutputConfig = {}  # type: ignore[typeddict-item]
    if "Outputs" in data:
        import capo_sagemaker.types.processing_outputs

        out["outputs"] = (
            capo_sagemaker.types.processing_outputs.deserialize_aws_json_1_1(
                data["Outputs"]
            )
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
