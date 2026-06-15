"""Generated from Smithy shape ``com.amazonaws.sagemaker#FlowDefinitionOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.s3_uri


class FlowDefinitionOutputConfig(TypedDict):
    s3_output_path: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    r"""<p>The Amazon S3 path where the object containing human output will be made available.</p> <p>To learn more about the format of Amazon A2I output data, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-output-data.html\">Amazon A2I Output Data</a>.</p>"""
    kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Key Management Service (KMS) key ID for server-side encryption.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowDefinitionOutputConfig) -> dict:
    out: dict = {}
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlowDefinitionOutputConfig:
    out: FlowDefinitionOutputConfig = {}  # type: ignore[typeddict-item]
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
