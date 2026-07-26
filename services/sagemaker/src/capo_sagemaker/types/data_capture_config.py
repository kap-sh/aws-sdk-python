"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataCaptureConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.capture_content_type_header
    import capo_sagemaker.types.capture_option_list
    import capo_sagemaker.types.destination_s3_uri
    import capo_sagemaker.types.enable_capture
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.sampling_percentage


class DataCaptureConfig(TypedDict, closed=True):
    enable_capture: NotRequired["capo_sagemaker.types.enable_capture.EnableCapture"]
    """<p>Whether data capture should be enabled or disabled (defaults to enabled).</p>"""
    initial_sampling_percentage: NotRequired[
        "capo_sagemaker.types.sampling_percentage.SamplingPercentage"
    ]
    """<p>The percentage of requests SageMaker AI will capture. A lower value is recommended for Endpoints with high traffic.</p>"""
    destination_s3_uri: NotRequired[
        "capo_sagemaker.types.destination_s3_uri.DestinationS3Uri"
    ]
    """<p>The Amazon S3 location used to capture the data.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Resource Name (ARN) of an Key Management Service key that SageMaker AI uses to encrypt the captured data at rest using Amazon S3 server-side encryption.</p> <p>The KmsKeyId can be any of the following formats: </p> <ul> <li> <p>Key ID: <code>1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Key ARN: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code> </p> </li> <li> <p>Alias name: <code>alias/ExampleAlias</code> </p> </li> <li> <p>Alias name ARN: <code>arn:aws:kms:us-west-2:111122223333:alias/ExampleAlias</code> </p> </li> </ul>"""
    capture_options: NotRequired[
        "capo_sagemaker.types.capture_option_list.CaptureOptionList"
    ]
    """<p>Specifies data Model Monitor will capture. You can configure whether to collect only input, only output, or both</p>"""
    capture_content_type_header: NotRequired[
        "capo_sagemaker.types.capture_content_type_header.CaptureContentTypeHeader"
    ]
    """<p>Configuration specifying how to treat different headers. If no headers are specified SageMaker AI will by default base64 encode when capturing the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataCaptureConfig) -> dict:
    out: dict = {}
    if "enable_capture" in value:
        out["EnableCapture"] = value["enable_capture"]
    if "initial_sampling_percentage" in value:
        out["InitialSamplingPercentage"] = value["initial_sampling_percentage"]
    if "destination_s3_uri" in value:
        out["DestinationS3Uri"] = value["destination_s3_uri"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "capture_options" in value:
        import capo_sagemaker.types.capture_option_list

        out["CaptureOptions"] = (
            capo_sagemaker.types.capture_option_list.serialize_aws_json_1_1(
                value["capture_options"]
            )
        )
    if "capture_content_type_header" in value:
        import capo_sagemaker.types.capture_content_type_header

        out["CaptureContentTypeHeader"] = (
            capo_sagemaker.types.capture_content_type_header.serialize_aws_json_1_1(
                value["capture_content_type_header"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataCaptureConfig:
    out: DataCaptureConfig = {}  # type: ignore[typeddict-item]
    if "EnableCapture" in data:
        out["enable_capture"] = data["EnableCapture"]
    if "InitialSamplingPercentage" in data:
        out["initial_sampling_percentage"] = data["InitialSamplingPercentage"]
    if "DestinationS3Uri" in data:
        out["destination_s3_uri"] = data["DestinationS3Uri"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "CaptureOptions" in data:
        import capo_sagemaker.types.capture_option_list

        out["capture_options"] = (
            capo_sagemaker.types.capture_option_list.deserialize_aws_json_1_1(
                data["CaptureOptions"]
            )
        )
    if "CaptureContentTypeHeader" in data:
        import capo_sagemaker.types.capture_content_type_header

        out["capture_content_type_header"] = (
            capo_sagemaker.types.capture_content_type_header.deserialize_aws_json_1_1(
                data["CaptureContentTypeHeader"]
            )
        )
    return out
