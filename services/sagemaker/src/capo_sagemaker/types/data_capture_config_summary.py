"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataCaptureConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.capture_status
    import capo_sagemaker.types.destination_s3_uri
    import capo_sagemaker.types.enable_capture
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.sampling_percentage


class DataCaptureConfigSummary(TypedDict, closed=True):
    enable_capture: NotRequired["capo_sagemaker.types.enable_capture.EnableCapture"]
    """<p>Whether data capture is enabled or disabled.</p>"""
    capture_status: NotRequired["capo_sagemaker.types.capture_status.CaptureStatus"]
    """<p>Whether data capture is currently functional.</p>"""
    current_sampling_percentage: NotRequired[
        "capo_sagemaker.types.sampling_percentage.SamplingPercentage"
    ]
    """<p>The percentage of requests being captured by your Endpoint.</p>"""
    destination_s3_uri: NotRequired[
        "capo_sagemaker.types.destination_s3_uri.DestinationS3Uri"
    ]
    """<p>The Amazon S3 location being used to capture the data.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key being used to encrypt the data in Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCaptureConfigSummary) -> dict:
    out: dict = {}
    if "enable_capture" in value:
        out["EnableCapture"] = value["enable_capture"]
    if "capture_status" in value:
        import capo_sagemaker.types.capture_status

        out["CaptureStatus"] = (
            capo_sagemaker.types.capture_status.serialize_aws_json_1_1(
                value["capture_status"]
            )
        )
    if "current_sampling_percentage" in value:
        out["CurrentSamplingPercentage"] = value["current_sampling_percentage"]
    if "destination_s3_uri" in value:
        out["DestinationS3Uri"] = value["destination_s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataCaptureConfigSummary:
    out: DataCaptureConfigSummary = {}  # type: ignore[typeddict-item]
    if "EnableCapture" in data:
        out["enable_capture"] = data["EnableCapture"]
    if "CaptureStatus" in data:
        import capo_sagemaker.types.capture_status

        out["capture_status"] = (
            capo_sagemaker.types.capture_status.deserialize_aws_json_1_1(
                data["CaptureStatus"]
            )
        )
    if "CurrentSamplingPercentage" in data:
        out["current_sampling_percentage"] = data["CurrentSamplingPercentage"]
    if "DestinationS3Uri" in data:
        out["destination_s3_uri"] = data["DestinationS3Uri"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
