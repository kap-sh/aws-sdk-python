"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetStorageLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.kms_key_arn
    import aws_sdk_lex_models_v2.types.s3_bucket_name
    import aws_sdk_lex_models_v2.types.s3_object_path


class TestSetStorageLocation(TypedDict, closed=True):
    s3_bucket_name: "aws_sdk_lex_models_v2.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon S3 bucket in which the test set is stored.</p>"""
    s3_path: "aws_sdk_lex_models_v2.types.s3_object_path.S3ObjectPath"
    """<p>The path inside the Amazon S3 bucket where the test set is stored.</p>"""
    kms_key_arn: NotRequired["aws_sdk_lex_models_v2.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of an Amazon Web Services Key Management Service (KMS) key for encrypting the test set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetStorageLocation) -> dict:
    out: dict = {}
    out["s3BucketName"] = value["s3_bucket_name"]
    out["s3Path"] = value["s3_path"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> TestSetStorageLocation:
    out: TestSetStorageLocation = {}  # type: ignore[typeddict-item]
    if "s3BucketName" in data:
        out["s3_bucket_name"] = data["s3BucketName"]
    else:
        raise DeserializationError("TestSetStorageLocation.s3_bucket_name required")
    if "s3Path" in data:
        out["s3_path"] = data["s3Path"]
    else:
        raise DeserializationError("TestSetStorageLocation.s3_path required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
