"""Generated from Smithy shape ``com.amazonaws.glue#S3EncryptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.s3_encryption

S3EncryptionList: TypeAlias = list["aws_sdk_glue.types.s3_encryption.S3Encryption"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3EncryptionList) -> list:
    import aws_sdk_glue.types.s3_encryption

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.s3_encryption.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> S3EncryptionList:
    import aws_sdk_glue.types.s3_encryption

    out: S3EncryptionList = []
    for item in data:
        out.append(aws_sdk_glue.types.s3_encryption.deserialize_aws_json_1_1(item))
    return out
