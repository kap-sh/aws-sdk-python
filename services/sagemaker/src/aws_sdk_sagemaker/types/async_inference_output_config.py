"""Generated from Smithy shape ``com.amazonaws.sagemaker#AsyncInferenceOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.async_inference_notification_config
    import aws_sdk_sagemaker.types.destination_s3_uri
    import aws_sdk_sagemaker.types.kms_key_id


class AsyncInferenceOutputConfig(TypedDict):
    kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key that SageMaker uses to encrypt the asynchronous inference output in Amazon S3.</p> <p/>"""
    s3_output_path: NotRequired[
        "aws_sdk_sagemaker.types.destination_s3_uri.DestinationS3Uri"
    ]
    """<p>The Amazon S3 location to upload inference responses to.</p>"""
    notification_config: NotRequired[
        "aws_sdk_sagemaker.types.async_inference_notification_config.AsyncInferenceNotificationConfig"
    ]
    """<p>Specifies the configuration for notifications of inference results for asynchronous inference.</p>"""
    s3_failure_path: NotRequired[
        "aws_sdk_sagemaker.types.destination_s3_uri.DestinationS3Uri"
    ]
    """<p>The Amazon S3 location to upload failure inference responses to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsyncInferenceOutputConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "notification_config" in value:
        import aws_sdk_sagemaker.types.async_inference_notification_config

        out["NotificationConfig"] = (
            aws_sdk_sagemaker.types.async_inference_notification_config.serialize_aws_json_1_1(
                value["notification_config"]
            )
        )
    if "s3_failure_path" in value:
        out["S3FailurePath"] = value["s3_failure_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AsyncInferenceOutputConfig:
    out: AsyncInferenceOutputConfig = {}  # type: ignore[typeddict-item]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    if "NotificationConfig" in data:
        import aws_sdk_sagemaker.types.async_inference_notification_config

        out["notification_config"] = (
            aws_sdk_sagemaker.types.async_inference_notification_config.deserialize_aws_json_1_1(
                data["NotificationConfig"]
            )
        )
    if "S3FailurePath" in data:
        out["s3_failure_path"] = data["S3FailurePath"]
    return out
