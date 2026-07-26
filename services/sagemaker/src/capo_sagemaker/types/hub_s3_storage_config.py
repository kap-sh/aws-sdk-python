"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubS3StorageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.s3_output_path


class HubS3StorageConfig(TypedDict, closed=True):
    s3_output_path: NotRequired["capo_sagemaker.types.s3_output_path.S3OutputPath"]
    """<p>The Amazon S3 bucket prefix for hosting hub content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubS3StorageConfig) -> dict:
    out: dict = {}
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HubS3StorageConfig:
    out: HubS3StorageConfig = {}  # type: ignore[typeddict-item]
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    return out
