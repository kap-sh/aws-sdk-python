"""Generated from Smithy shape ``com.amazonaws.sfn#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.encryption_type
    import aws_sdk_sfn.types.kms_data_key_reuse_period_seconds
    import aws_sdk_sfn.types.kms_key_id


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired["aws_sdk_sfn.types.kms_key_id.KmsKeyId"]
    """<p>An alias, alias ARN, key ID, or key ARN of a symmetric encryption KMS key to encrypt data. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.</p>"""
    kms_data_key_reuse_period_seconds: NotRequired[
        "aws_sdk_sfn.types.kms_data_key_reuse_period_seconds.KmsDataKeyReusePeriodSeconds"
    ]
    """<p>Maximum duration that Step Functions will reuse data keys. When the period expires, Step Functions will call <code>GenerateDataKey</code>. Only applies to customer managed keys.</p>"""
    type: "aws_sdk_sfn.types.encryption_type.EncryptionType"
    """<p>Encryption type</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "kms_data_key_reuse_period_seconds" in value:
        out["kmsDataKeyReusePeriodSeconds"] = value["kms_data_key_reuse_period_seconds"]
    import aws_sdk_sfn.types.encryption_type

    out["type"] = aws_sdk_sfn.types.encryption_type.serialize_aws_json_1_0(
        value["type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "kmsDataKeyReusePeriodSeconds" in data:
        out["kms_data_key_reuse_period_seconds"] = data["kmsDataKeyReusePeriodSeconds"]
    if "type" in data:
        import aws_sdk_sfn.types.encryption_type

        out["type"] = aws_sdk_sfn.types.encryption_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("EncryptionConfiguration.type required")
    return out
