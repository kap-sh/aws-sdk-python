"""Generated from Smithy shape ``com.amazonaws.dsql#EncryptionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dsql.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dsql.types.encryption_status
    import aws_sdk_dsql.types.encryption_type
    import aws_sdk_dsql.types.kms_key_arn


class EncryptionDetails(TypedDict):
    encryption_type: "aws_sdk_dsql.types.encryption_type.EncryptionType"
    """<p>The type of encryption that protects the data on your cluster.</p>"""
    kms_key_arn: NotRequired["aws_sdk_dsql.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key that encrypts data in the cluster.</p>"""
    encryption_status: "aws_sdk_dsql.types.encryption_status.EncryptionStatus"
    """<p>The status of encryption for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionDetails) -> dict:
    out: dict = {}
    import aws_sdk_dsql.types.encryption_type

    out["encryptionType"] = aws_sdk_dsql.types.encryption_type.serialize_json(
        value["encryption_type"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    import aws_sdk_dsql.types.encryption_status

    out["encryptionStatus"] = aws_sdk_dsql.types.encryption_status.serialize_json(
        value["encryption_status"]
    )
    return out


def deserialize_json(data: dict) -> EncryptionDetails:
    out: EncryptionDetails = {}  # type: ignore[typeddict-item]
    if "encryptionType" in data:
        import aws_sdk_dsql.types.encryption_type

        out["encryption_type"] = aws_sdk_dsql.types.encryption_type.deserialize_json(
            data["encryptionType"]
        )
    else:
        raise DeserializationError("EncryptionDetails.encryption_type required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "encryptionStatus" in data:
        import aws_sdk_dsql.types.encryption_status

        out["encryption_status"] = (
            aws_sdk_dsql.types.encryption_status.deserialize_json(
                data["encryptionStatus"]
            )
        )
    else:
        raise DeserializationError("EncryptionDetails.encryption_status required")
    return out
