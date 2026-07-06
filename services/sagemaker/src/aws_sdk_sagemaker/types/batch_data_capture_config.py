"""Generated from Smithy shape ``com.amazonaws.sagemaker#BatchDataCaptureConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.s3_uri


class BatchDataCaptureConfig(TypedDict, closed=True):
    destination_s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 location being used to capture the data.</p>"""
    kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service key that SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the batch transform job.</p> <p>The KmsKeyId can be any of the following formats: </p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias name ARN: <code>arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul>"""
    generate_inference_id: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Flag that indicates whether to append inference id to the output.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDataCaptureConfig) -> dict:
    out: dict = {}
    if "destination_s3_uri" in value:
        out["DestinationS3Uri"] = value["destination_s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "generate_inference_id" in value:
        out["GenerateInferenceId"] = value["generate_inference_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDataCaptureConfig:
    out: BatchDataCaptureConfig = {}  # type: ignore[typeddict-item]
    if "DestinationS3Uri" in data:
        out["destination_s3_uri"] = data["DestinationS3Uri"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "GenerateInferenceId" in data:
        out["generate_inference_id"] = data["GenerateInferenceId"]
    return out
