"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GrammarSlotTypeSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.kms_key_arn
    import aws_sdk_lex_models_v2.types.s3_bucket_name
    import aws_sdk_lex_models_v2.types.s3_object_path


class GrammarSlotTypeSource(TypedDict):
    s3_bucket_name: "aws_sdk_lex_models_v2.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon S3 bucket that contains the grammar source.</p>"""
    s3_object_key: "aws_sdk_lex_models_v2.types.s3_object_path.S3ObjectPath"
    """<p>The path to the grammar in the Amazon S3 bucket.</p>"""
    kms_key_arn: NotRequired["aws_sdk_lex_models_v2.types.kms_key_arn.KmsKeyArn"]
    """<p>The KMS key required to decrypt the contents of the grammar, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrammarSlotTypeSource) -> dict:
    out: dict = {}
    out["s3BucketName"] = value["s3_bucket_name"]
    out["s3ObjectKey"] = value["s3_object_key"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GrammarSlotTypeSource:
    out: GrammarSlotTypeSource = {}  # type: ignore[typeddict-item]
    if "s3BucketName" in data:
        out["s3_bucket_name"] = data["s3BucketName"]
    else:
        raise DeserializationError("GrammarSlotTypeSource.s3_bucket_name required")
    if "s3ObjectKey" in data:
        out["s3_object_key"] = data["s3ObjectKey"]
    else:
        raise DeserializationError("GrammarSlotTypeSource.s3_object_key required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
