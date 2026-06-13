"""Generated from Smithy shape ``com.amazonaws.braket#JobOutputDataConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.s3_path
    import aws_sdk_braket.types.string2048


class JobOutputDataConfig(TypedDict):
    kms_key_id: NotRequired["aws_sdk_braket.types.string2048.String2048"]
    """<p>The AWS Key Management Service (AWS KMS) key that Amazon Braket uses to encrypt the hybrid job training artifacts at rest using Amazon S3 server-side encryption.</p>"""
    s3_path: "aws_sdk_braket.types.s3_path.S3Path"
    """<p>Identifies the S3 path where you want Amazon Braket to store the hybrid job training artifacts. For example, <code>s3://bucket-name/key-name-prefix</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobOutputDataConfig) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    out["s3Path"] = value["s3_path"]
    return out


def deserialize_json(data: dict) -> JobOutputDataConfig:
    out: JobOutputDataConfig = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "s3Path" in data:
        out["s3_path"] = data["s3Path"]
    else:
        raise DeserializationError("JobOutputDataConfig.s3_path required")
    return out
